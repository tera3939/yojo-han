from pymongo import MongoClient

import config


def create_users(db):
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
    print("setup users")
    user = db[config.USER_COLLECTION]
    user.create_index([("actor.id", 1)], unique=True)
    user.create_index([("created_at", -1)])


def create_db():
    print("connection")
    con = MongoClient()
    db = con[config.APP_NAME]

    create_users(db)
    print("done")


if __name__ == "__main__":
    create_db()
