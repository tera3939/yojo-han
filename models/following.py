from datetime import datetime

from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database

import config


class Following:
    def __init__(self, db: Database):
        self.__following: Collection = db[config.FOLLOWING_COLLECTION]

    def add(self, following):
        # TODO: DuplicateKeyErrorの対応、どうする?
        self.__following.insert_one({
            "following": following,
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str):
        return self.__following.find_one({"$or": [{"following.preferredUsername": name}, {"following.name": name}]})

    def get_list(self) -> Cursor:
        return self.__following.find({})

    def remove(self, following_id: str):
        self.__following.delete_one({"following.id": following_id})

    def count(self):
        return self.__following.estimated_document_count()
