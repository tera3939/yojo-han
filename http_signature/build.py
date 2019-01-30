import base64

from Crypto.PublicKey.RSA import RsaKey

from .util import Util


def build(method: str, resource: str, target_host: str, date: str, key_id: str, keypair: RsaKey) -> str:
    """
    雑にHTTP Signatureを生成するぞ
    :param method: リクエストメソッド
    :param resource: 叩くリソース
    :param target_host: 送信先のホスト名
    :param date: 日付 RFC 1123 Date Representationで頼む
    :param key_id: 送信元アクターのpublicKey.id
    :param keypair: 送信元アクターのプライベートキー
    :return: HTTP Signature文字列。リクエストヘッダのSignatureに添えてね
    """
    http_header = f"(request-target): {method.lower()} {resource}\nhost: {target_host}\ndate: {date}"
    header_sign = base64.standard_b64encode(Util.sign_message(http_header, keypair)).decode()
    http_signature = f'keyId="{key_id}",algorithm="rsa-sha256",headers="(request-target) host date",' +\
                     f'signature="{header_sign}"'
    return http_signature
