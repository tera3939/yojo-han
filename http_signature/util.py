from time import mktime
from datetime import datetime
from wsgiref.handlers import format_date_time

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey.RSA import RsaKey
from Crypto.Signature import pkcs1_15


class Util:
    @staticmethod
    def sign_message(message: str, keypair: RsaKey) -> bytes:
        message_hash = SHA256.new(message.encode())
        signature = pkcs1_15.new(keypair).sign(message_hash)
        return signature

    @staticmethod
    def verify_message(message: str, signature: bytes, pubkey: RsaKey) -> bool:
        message_hash = SHA256.new(message.encode())
        try:
            pkcs1_15.new(pubkey).verify(message_hash, signature)
            return True
        except ValueError:
            return False

    @staticmethod
    def fetch_json(url: str):
        headers = {"Accept": "application/activity+json, application/ld+json"}
        res = requests.request("GET", url, headers=headers)
        return res.json()

    @staticmethod
    def get_actor(key_id: str):
        key_properties = ["publicKeyPem", "owner"]
        actor_properties = ["id", "publicKey", "inbox"]
        actor = None
        key_object = Util.fetch_json(key_id)
        if all((key in key_object for key in key_properties)):
            actor = Util.fetch_json(key_object["owner"])
            actor["publicKey"] = key_object
        elif all((key in key_object for key in actor_properties)):
            actor = key_object
        return actor

    @staticmethod
    def get_time() -> str:
        now = datetime.now()
        stamp = mktime(now.timetuple())
        date = format_date_time(stamp)
        return date
