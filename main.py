import json

from flask import Flask, Response, render_template

import setting

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<user_name>")
def user(user_name: str) -> Response:
    actor_object = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": route_url(f"/user/{user_name}"),
        "type": "Person",
        "name": setting.USERNAME,
        "preferredUsername": setting.USERNAME,
        "inbox": route_url("/inbox"),

        "publicKey": {
            "@context": "https://w3id.org/security/v1",
            "type": "Key",
            "id": route_url(f"/user/{user_name}#main-key"),
            "owner": route_url(f"/user/{user_name}"),
            "publicKeyPem": setting.KEYPAIR.publickey().export_key().decode()
        }
    }
    if user_name != setting.USERNAME:
        return Response(status=404)
    return Response(json.dumps(actor_object), content_type="application/activity+json")


def route_url(path: str) -> str:
    return f"https://{setting.DOMAIN}{path}"


if __name__ == "__main__":
    app.run(debug=True)
