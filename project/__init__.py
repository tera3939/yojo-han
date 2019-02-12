import json
import pprint
import re
from typing import Optional
from urllib.parse import urlparse

import requests
from flask import Flask, Response, request, render_template
from pymongo import MongoClient

from project import config
from project import http_signature
from project import util
from project.activity_stream import Actor, Activity, ActivityType
from project.models import User, Follower

app = Flask(__name__)
DB = MongoClient()[config.DB_NAME]
ACCT = re.compile(r"^acct:(\w+)@([\w.-]+)")


@app.route("/")
def index():
    global DB
    user_collection = User(DB)
    u = user_collection.get()["actor"]
    return render_template("index.html", user=u)


@app.route("/user/<user_name>")
def user(user_name: str) -> Response:
    global DB

    actor_object = User(DB).get_by_name(user_name)

    if user_name != config.USERNAME:
        return Response(status=404)

    return Response(json.dumps(actor_object["actor"]), content_type="application/activity+json")


@app.route("/follower")
def follower():
    global DB

    f = Follower(DB)
    follower_list = f.get_list().sort([("created_at", -1)])

    return render_template("follower.html", follower_list=follower_list)


@app.route("/inbox", methods=["POST"])
def inbox() -> Response:
    global DB

    if request.method == "POST" and request.is_json:
        result = http_signature.verify(request)

        if result is None:
            return Response(status=404)

        request_body, actor = result
        activity = Activity(json.loads(request_body.decode()))
        activity_type = activity.get_type()

        if activity_type == ActivityType.FOLLOW:
            follower_collection = Follower(DB)
            follower_collection.add(actor)
        elif activity_type == ActivityType.UNDO:
            follower_collection = Follower(DB)
            follower_collection.remove(actor["id"])
        else:
            pass
    else:
        return Response(status=404)

    return Response("OK", status=202)


@app.route("/outbox", methods=["POST"])
def outbox() -> Response:
    global DB

    if not request.is_json:
        return Response("Error: Request is not json", status=404)

    activity = Activity(json.loads(request.data.decode()))

    # TODO: ActivityのほうにidのURI探すメソッド入れる方がよくない?わからん……
    actor_id = get_id_by_activity(activity.get_activity_object())
    if actor_id is None:
        return Response("Error: Not Found Object ID", status=404)

    actor_dict = util.get_actor(actor_id)
    if actor_dict is None:
        return Response("Error: Actor is None", status=404)

    actor = Actor(actor_dict)

    if actor.get_inbox() is None:
        return Response("Error: Actor don't have inbox", status=404)

    inbox_url = actor.get_inbox()
    url = urlparse(inbox_url)
    host = url.netloc
    resource = url.path
    headers = {
        "Host": host,
        "Date": util.get_time(),
        "Accept": 'application/activity+json,application/ld+json;profile="https://www.w3.org/ns/activitystreams"',
        "Content-Type": "application/activity+json;charset=UTF-8"
    }

    user_collection = User(DB).get()
    user = Actor(user_collection["actor"])
    key_id = user.get_public_key()["id"]
    signature = http_signature.build("POST", resource, headers, key_id, config.KEYPAIR)
    headers["Signature"] = signature

    result = requests.request("POST", inbox, headers=headers, json=activity)

    return Response(result.text, status=result.status_code)


@app.route("/.well-known/webfinger")
def webfinger() -> Response:
    global ACCT

    resource = request.args.get("resource")

    if resource is None:
        return Response(status=404)

    matched_resources = ACCT.match(resource)

    if matched_resources is None:
        return Response(status=404)

    user_id, domain = matched_resources.groups()
    j = {
        "subject": f"acct:{user_id}@{domain}",
        "links": [{
            "rel": "self",
            "type": "application/activity+json",
            "href": f"https://{domain}/user/{user_id}"
        }]
    }

    if user_id != config.USERNAME or domain != config.DOMAIN:
        return Response(status=404)

    return Response(json.dumps(j), content_type="application/json")


@app.route('/.well-known/host-meta')
def host_meta() -> Response:
    template_url = route_url("/.well-known/webfinger?resource={uri}")
    xml_str = f'''<?xml version="1.0" encoding="UTF-8"?>
<XRD xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">
  <Link rel="lrdd" type="application/xrd+xml" template="{template_url}"/>
</XRD>'''

    return Response(xml_str, content_type='application/xrd+xml')


def route_url(path: str) -> str:
    return f"https://{config.DOMAIN}{path}"


def get_id_by_activity(act) -> Optional[str]:
    def __inner(activity, count: int):
        if count > 3:
            return None

        # TODO: 流石にこれはどうにかしたい
        if activity["type"] in ["Application", "Group", "Organization", "Person", "Service"]:
            # if activity is ActorObject
            if "id" in activity:
                return activity["id"]
            else:
                return None

        if "object" in activity:
            if isinstance(activity["object"], str):
                return activity["object"]
            return __inner(activity["object"], count+1)
        return None

    return __inner(act, 0)
