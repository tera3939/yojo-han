from pymongo import MongoClient
from pymongo.database import Database

import config


def create_user(db: Database):
    """
    {
        "actor": { ActorObject },
        "password": PasswordHash,
        "created_at": ISOData Actorの登録日時,
        "_id": MongoDBが作るユニークID
    }
    :param db: データベースへのコネクション
    :return: None
    """
    print("setup user collection")
    user = db[config.USER_COLLECTION]
    user.create_index([("actor.id", 1)], unique=True)
    user.create_index([("created_at", -1)])


def create_db():
    print("connection")
    con = MongoClient()
    db = con[config.APP_NAME]

    create_user(db)
    print("done")


if __name__ == "__main__":
    create_db()
