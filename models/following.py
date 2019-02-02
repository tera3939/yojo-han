from datetime import datetime

from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database

import config


class Following:
    def __init__(self, db: Database):
        self.__followers: Collection = db[config.FOLLOWING_COLLECTION]

    def add(self, following):
        self.__followers.insert_one({
            "following": following,
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str):
        return self.__followers.find_one({"$or": [{"following.preferredUsername": name}, {"following.name": name}]})

    def get_list(self) -> Cursor:
        return self.__followers.find({})

    def remove(self, following_id: str):
        self.__followers.delete_one({"following.id": following_id})

    def count(self):
        count = self.__followers.estimated_document_count()
        return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": "OrderedCollection",
            "totalItems": count
        }
