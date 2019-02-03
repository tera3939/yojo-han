import base64
from typing import Dict, Optional

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from Crypto.Signature import pkcs1_15
from flask import Request

import util


def sign_message(message: str, keypair: RsaKey) -> bytes:
    message_hash = SHA256.new(message.encode())
    signature = pkcs1_15.new(keypair).sign(message_hash)
    return signature


def verify_message(message: str, signature: bytes, pubkey: RsaKey) -> bool:
    message_hash = SHA256.new(message.encode())
    try:
        pkcs1_15.new(pubkey).verify(message_hash, signature)
        return True
    except ValueError:
        return False


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


def parse_signature_string(signature_string: str) -> Dict[str, str]:
    parts = signature_string.split(",")
    params = dict(((key, value.strip('"')) for key, value in
                   map(lambda part: part.split("=", 1), parts)))
    return params


def build(method: str, resource: str, headers: Dict[str, str], key_id: str, keypair: RsaKey) -> str:
    """
    HTTP Signatureを生成するぞ
    :param method: HTTPリクエストのメソッド
    :param resource: リソース
    :param headers: HTTPリクエストのヘッダー
    :param key_id: 送信元アクターのpublicKey.id
    :param keypair: 送信元アクターのプライベートキー
    :return: HTTP Signature文字列。リクエストヘッダのSignatureに添えてね
    """
    headers_string = "(request-target) " + " ".join(headers.keys())
    # TODO: digestに対応
    signature_string = build_signature_string(method, resource, headers, None, headers_string)
    signature = base64.standard_b64encode(sign_message(signature_string, keypair)).decode()

    # TODO: algorithmをrsa-sha256に固定してるけどいいんすか?
    http_signature = f'keyId="{key_id}",algorithm="rsa-sha256",headers="{headers_string}",signature="{signature}"'

    return http_signature


def verify(request: Request):
    """
    POSTされたRequestをHTTP Signatureで検証し、成功したらデータと送信元のActorObjectを返す。
    :return:
        body: POSTリクエストのデータ
        actor: 送信したアクターのActorObject
    """
    signature_params = parse_signature_string(request.headers["Signature"])
    body: bytes = request.data
    key_id: str = signature_params["keyId"]
    actor = util.get_actor(key_id)
    signature: str = signature_params["signature"]

    signed_string = build_signature_string(request.method, request.path, request.headers,
                                           body, signature_params["headers"])
    public_key = RSA.import_key(actor["publicKey"]["publicKeyPem"])

    decoded_signature = base64.b64decode(signature)
    if verify_message(signed_string, decoded_signature, public_key):
        return body, actor
    else:
        return None
