import base64

from Crypto.PublicKey import RSA
from flask import Request

from .util import Util


def verify(request: Request):
    """
    POSTされたRequestをHTTP Signatureで検証し、成功したらデータと送信元のActorObjectを返す。
    :return:
        body: POSTリクエストのデータ
        actor: 送信したアクターのActorObject
    """
    signature_params = Util.parse_signature_string(request.headers["Signature"])
    body: bytes = request.data
    key_id: str = signature_params["keyId"]
    actor = Util.get_actor(key_id)
    signature: str = signature_params["signature"]

    signed_string = Util.build_signature_string(request.method, request.path, request.headers,
                                                body, signature_params["headers"])
    public_key = RSA.import_key(actor["publicKey"]["publicKeyPem"])

    decoded_signature = base64.b64decode(signature)
    if Util.verify_message(signed_string, decoded_signature, public_key):
        return body, actor
    else:
        return None
