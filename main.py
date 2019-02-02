import json
import pprint
import re

from flask import Flask, Response, request, render_template
from pymongo import MongoClient

import config
from models import User

app = Flask(__name__)
DB = MongoClient()[config.APP_NAME]
ACCT = re.compile(r"^acct:(\w+)@([\w.-]+)")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<user_name>")
def user(user_name: str) -> Response:
    global DB
    actor_object = User(DB).get_by_name(user_name)
    if user_name != config.USERNAME:
        return Response(status=404)
    pprint.pprint(actor_object["actor"])
    pprint.pprint(actor_object["actor"])
    return Response(json.dumps(actor_object["actor"]), content_type="application/activity+json")


@app.route("/inbox", methods=["POST"])
def inbox() -> Response:
    return Response("OK", status=200)


@app.route("/outbox", methods=["POST"])
def outbox() -> Response:
    return Response("OK", status=200)


@app.route("/.well-known/webfinger")
def webfinger() -> Response:
    global ACCT
    resource = request.args.get("resource")
    user_id, domain = ACCT.match(resource).groups()
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
    return Response(xml_str, headers={'Content-Type': 'application/xrd+xml'})


def route_url(path: str) -> str:
    return f"https://{config.DOMAIN}{path}"


if __name__ == "__main__":
    app.run(debug=True)
