from datetime import datetime

from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database

import config


class Follower:
    def __init__(self, db: Database):
        self.__followers: Collection = db[config.FOLLOWER_COLLECTION]

    def add(self, follower):
        # TODO: DuplicateKeyErrorの対応、どうする?
        self.__followers.insert_one({
            "follower": follower,
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str):
        return self.__followers.find_one({"$or": [{"follower.preferredUsername": name}, {"follower.name": name}]})

    def get_list(self) -> Cursor:
        return self.__followers.find({})

    def remove(self, following_id: str):
        self.__followers.delete_one({"follower.id": following_id})

    def count(self):
        return self.__followers.estimated_document_count()
