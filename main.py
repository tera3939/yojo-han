import json
import pprint
import re
from urllib.parse import urlparse

import requests
from flask import Flask, Response, request, render_template
from pymongo import MongoClient

import config
import http_signature
import util
from activity_type import ActivityType
from models import User, Follower

app = Flask(__name__)
DB = MongoClient()[config.APP_NAME]
ACCT = re.compile(r"^acct:(\w+)@([\w.-]+)")


@app.route("/")
def index():
    return render_template("base.html")


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
        activity = json.loads(request_body.decode())
        activity_type = activity["type"]
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
    return Response("OK", status=200)


@app.route("/outbox", methods=["GET", "POST"])
def outbox() -> Response:
    global DB

    if request.method == "POST" and request.is_json:
        activity = json.loads(request.data.decode())
        pprint.pprint(activity)

        url = urlparse(activity["object"])
        host = url.netloc
        resource = url.path
        headers = {
            "Host": host,
            "Date": util.get_time(),
            "Accept": "application/ld+json,application/activity+json",
            "Content-Type": "application/ld+json"
        }
        user = User(DB).get()
        key_id = user["actor"]["publicKey"]["id"]
        signature = http_signature.build("POST", resource, headers, key_id, config.KEYPAIR)
        headers["Signature"] = signature

        actor = util.get_actor(url.geturl())
        if actor is None:
            return Response("Error: actor is None", status=404)
        if "outbox" in actor:
            outbox = actor["outbox"]
            pprint.pprint(actor)
            pprint.pprint(headers)
            r = requests.request("POST", outbox, headers=headers, data=activity)
            return Response(r.text, status=200)
        return Response(status=404)
    else:
        url = urlparse("https://mastodon.cloud/users/tera/inbox")
        host = url.netloc
        resource = url.path
        headers = {
            "Host": host,
            "Date": util.get_time(),
            "Accept": "application/ld+json,application/activity+json",
            "Content-Type": "application/ld+json"
        }
        user = User(DB).get()
        key_id = user["actor"]["publicKey"]["id"]
        signature = http_signature.build("POST", resource, headers, key_id, config.KEYPAIR)
        headers["Signature"] = signature
        pprint.pprint(headers)
        return Response(status=200)


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


if __name__ == "__main__":
    app.run(debug=True)
