from pymongo import MongoClient
from pymongo.database import Database

import config


def create_user(db: Database):
    """
    Userを格納するコレクション。Userは唯一人。
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


def create_following(db: Database):
    """
    UserがフォローしたActorを格納するコレクション。
    {
        "following": ActorObject フォローされたActor,
        "created_at": ISODate フォローした日時,
        "_id": MongoDBが作るユニークID
    }
    :param db: データベースへのコネクション
    :return: None
    """
    print("setup following collection")
    following = db[config.FOLLOWING_COLLECTION]
    following.create_index([("following.id", 1)], unique=True)
    following.create_index([("created_at", -1)])


def create_follower(db: Database):
    """
    UserをフォローしてきたActorを格納するコレクション。
    {
        "following": ActorObject フォローしてきたActor
        "created_at": ISODate フォローされた日時,
        "_id": MongoDBが作るユニークID
    }
    :param db: データベースへのコネクション
    :return: None
    """
    print("setup follower collection")
    following = db[config.FOLLOWING_COLLECTION]
    following.create_index([("follower.id", 1)], unique=True)
    following.create_index([("created_at", -1)])


def create_db():
    print("connection")
    con = MongoClient()
    db = con[config.APP_NAME]

    create_user(db)
    create_following(db)
    create_follower(db)

    print("done")


if __name__ == "__main__":
    create_db()
