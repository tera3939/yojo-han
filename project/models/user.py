from datetime import datetime

import bcrypt
from pymongo.collection import Collection
from pymongo.database import Database

from project import config
from project.json_type import Json


class User:
    def __init__(self, db: Database) -> None:
        # TODO: user用にコレクションを作ることは一人専用というコンセプトから離れているのでは?
        self.__user: Collection = db[config.USER_COLLECTION]

    def add(self, actor, password: bytes):
        # TODO: DuplicateKeyErrorの対応、どうする?
        self.__user.insert_one({
            "actor": actor,
            "password": bcrypt.hashpw(password, bcrypt.gensalt()),
            "created_at": datetime.now()
        })

    def get_by_name(self, name: str) -> Json:
        return self.__user.find_one({"$or": [{"actor.preferredUsername": name}, {"actor.name": name}]})

    def get(self) -> Json:
        # userは唯一人という前提のもと、この操作は正義。
        return self.__user.find_one({})
