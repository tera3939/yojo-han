import base64
from time import mktime
from datetime import datetime
from typing import Optional, Dict
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

    @staticmethod
    def build_signature_string(method: str, resource: str, headers: Dict[str, str], body: bytes, headers_string: Optional[str]) -> str:
        if headers_string is None:
            headers_string = "date"
        header_elements = []
        for header_name in headers_string.split(" "):
            if header_name == "(request-target)":
                method = method.lower()
                header_elements.append(f"(request-target): {method} {resource}")
            elif header_name == "digest":
                body_digest = SHA256.new(body)
                encoded_digest = base64.standard_b64encode(body_digest.digest()).decode()
                header_elements.append(f"digest: SHA-256={encoded_digest}")
            else:
                header = headers[header_name]
                header_elements.append(f"{header_name}: {header}")
        return "\n".join(header_elements)

    @staticmethod
    def parse_signature_string(signature_string: str) -> Dict[str, str]:
        parts = signature_string.split(",")
        params = dict(((key, value.strip('"')) for key, value in
                       map(lambda part: part.split("=", 1), parts)))
        return params
