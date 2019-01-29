import base64
from typing import Dict
from typing import Optional

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from flask import Request

from .util import Util


class Verification:
    def __init__(self, request: Request) -> None:
        self.request = request

    def verify(self):
        """
        POSTされたRequestをHTTP Signatureで検証し、成功したらデータと送信元のActorObjectを返す。
        :return:
            body: POSTリクエストのデータ
            actor: 送信したアクターのActorObject
        """
        signature_params = self.__parse()
        body: bytes = self.request.data
        key_id: str = signature_params["keyId"]
        actor = Util.get_actor(key_id)
        signature: str = signature_params["signature"]

        signed_string = self.__build(body, signature_params["headers"])
        public_key = RSA.import_key(actor["publicKey"]["publicKeyPem"])

        signature = base64.b64decode(signature)
        if Util.verify_message(signed_string, signature, public_key):
            return body, actor
        else:
            return None

    def __parse(self) -> Dict[str, str]:
        parts = self.request.headers["Signature"].split(",")
        params = dict(((key, value.strip('"')) for key, value in
                       map(lambda part: part.split("=", 1), parts)))
        return params

    def __build(self, body: bytes, signed_headers: Optional[str]) -> str:
        if signed_headers is None:
            signed_headers = "date"
        signed_string = ""
        for header_name in signed_headers.split(" "):
            if header_name == "(request-target)":
                method = self.request.method
                path = self.request.path
                signed_string += f"(request-target): {method} {path}\n"
            elif header_name == "digest":
                body_digest = SHA256.new(body)
                signed_string += f"digest: SHA-256={base64.standard_b64encode(body_digest.digest())}\n"
            else:
                header = self.request.headers[header_name]
                signed_string += f"{header_name}: {header}\n"
        return signed_string


def verify(request: Request):
    v = Verification(request)
    return v.verify()
