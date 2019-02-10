import json
from datetime import datetime
from functools import lru_cache
from time import mktime
from typing import Optional
from wsgiref.handlers import format_date_time

import requests

from project.json_type import Json


@lru_cache()
def fetch_json(url: str) -> Optional[Json]:
    headers = {"Accept": "application/activity+json, application/ld+json"}
    try:
        res = requests.request("GET", url, headers=headers)
        return json.loads(res.content.decode())
    except:
        # TODO: なんかいい感じの処理
        return None


def get_actor(key_id: str) -> Optional[Json]:
    key_properties = ["publicKeyPem", "owner"]
    actor_properties = ["id", "publicKey", "inbox"]
    actor = None
    key_object = fetch_json(key_id)
    if key_object is None:
        return None
    if all((key in key_object for key in key_properties)):
        # key_objectのtypeがKeyのときの処理
        actor = fetch_json(key_object["owner"])
        if actor is None:
            return None
        actor["publicKey"] = key_object
    elif all((key in key_object for key in actor_properties)):
        # key_objectがActorObjectのときの処理
        actor = key_object
    return actor


def get_time() -> str:
    now = datetime.now()
    stamp = mktime(now.timetuple())
    date = format_date_time(stamp)
    return date
