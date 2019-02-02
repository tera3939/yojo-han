import os.path
from Crypto.PublicKey import RSA


APP_NAME = "yojo-han"

USERNAME = "user_name"
DOMAIN = "domain.com"
PRIVATEKEY_FILE = "privatekey.pem"

if os.path.exists(PRIVATEKEY_FILE):
    with open(PRIVATEKEY_FILE, "r") as f:
        KEYPAIR = RSA.import_key(f.read())
else:
    with open(PRIVATEKEY_FILE, "wb") as f:
        KEYPAIR = RSA.generate(2048)
        f.write(KEYPAIR.export_key("PEM"))
