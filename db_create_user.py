from pymongo import MongoClient
from pymongo.database import Database

from models import User
import config


def route_url(path: str) -> str:
    return f"https://{config.DOMAIN}{path}"


def create_user(db: Database):
    """
        雑に適当なユーザーを詰め込む
    """
    user = User(db)
    print("add user:", config.USERNAME)
    user.add({
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": route_url(f"/user/{config.USERNAME}"),
        "type": "Person",
        "name": config.USERNAME,
        "preferredUsername": config.USERNAME,
        "inbox": route_url("/inbox"),

        "publicKey": {
            "@context": "https://w3id.org/security/v1",
            "type": "Key",
            "id": route_url(f"/user/{config.USERNAME}#main-key"),
            "owner": route_url(f"/user/{config.USERNAME}"),
            "publicKeyPem": config.KEYPAIR.publickey().export_key().decode()
        }
    }, b"hoge")
    print("done")


if __name__ == "__main__":
    db = MongoClient()[config.APP_NAME]
    create_user(db)
    db.close()
