from datetime import datetime

import bcrypt
from pymongo.collection import Collection
from pymongo.database import Database

import config


class User:
    def __init__(self, db: Database):
        self.__user: Collection = db[config.USER_COLLECTION]

    def add(self, actor, password: bytes):
        # TODO: DuplicateKeyErrorの対応、どうする?
        self.__user.insert_one({
            "actor": actor,
            "password": bcrypt.hashpw(password, bcrypt.gensalt()),
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str):
        return self.__user.find_one({"$or": [{"actor.preferredUsername": name}, {"actor.name": name}]})
