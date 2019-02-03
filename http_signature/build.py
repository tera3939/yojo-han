import base64
from typing import Dict

from Crypto.PublicKey.RSA import RsaKey

from .util import Util


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
    signature_string = Util.build_signature_string(method, resource, headers, None, headers_string)
    signature = base64.standard_b64encode(Util.sign_message(signature_string, keypair))

    # TODO: algorithmをrsa-sha256に固定してるけどいいんすか?
    http_signature = f'keyId="{key_id}",algorithm="rsa-sha256",headers="{headers_string}",signature="{signature}"'

    return http_signature
