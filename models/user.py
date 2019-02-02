from datetime import datetime

import bcrypt
from pymongo.collection import Collection

from main import DB


class User:
    def __init__(self):
        self.__user: Collection = DB["users"]

    def add(self, actor, password: bytes):
        # TODO: DuplicationErrorとかの対応
        self.__user.insert_one({
            "actor": actor,
            "password": bcrypt.hashpw(password, bcrypt.gensalt()),
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str):
        return self.__user.find_one({"$or": [{"preferredUsername": name}, {"name": name}]})
