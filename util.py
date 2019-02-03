from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time

import requests


def fetch_json(url: str):
    headers = {"Accept": "application/activity+json, application/ld+json"}
    res = requests.request("GET", url, headers=headers)
    return res.json()


def get_actor(key_id: str):
    key_properties = ["publicKeyPem", "owner"]
    actor_properties = ["id", "publicKey", "inbox"]
    actor = None
    key_object = fetch_json(key_id)
    if all((key in key_object for key in key_properties)):
        actor = fetch_json(key_object["owner"])
        actor["publicKey"] = key_object
    elif all((key in key_object for key in actor_properties)):
        actor = key_object
    return actor


def get_time() -> str:
    now = datetime.now()
    stamp = mktime(now.timetuple())
    date = format_date_time(stamp)
    return date
