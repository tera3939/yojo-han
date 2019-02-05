import json
from datetime import datetime
from functools import lru_cache
from time import mktime
from typing import Optional
from wsgiref.handlers import format_date_time

import requests

from json_type import Json


@lru_cache()
def fetch_json(url: str) -> Optional[Json]:
    headers = {"Accept": "application/activity+json, application/ld+json"}
    res = requests.request("GET", url, headers=headers)
    try:
        return json.loads(res.content.decode())
    except json.JSONDecodeError:
        return None


def get_actor(key_id: str) -> Optional[Json]:
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
