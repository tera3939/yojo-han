from typing import Optional

from project.activity_stream import Object_
from project.json_type import Json


class Actor(Object_):
    def __init__(self, _actor: Json) -> None:
        super().__init__(_actor)
        self.properties = ['inbox', 'outbox', 'following', 'followers', 'liked', 'streams', 'preferredUsername',
                           'endpoints', 'proxyUrl', 'oauthAuthorizationEndpoint', 'oauthTokenEndpoint',
                           'provideClientKey', 'signClientKey', 'sharedInbox', 'publicKey']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.inbox = "inbox"
        self.outbox = "outbox"
        self.following = "following"
        self.followers = "followers"
        self.liked = "liked"
        self.streams = "streams"
        self.preferred_username = "preferredUsername"
        self.endpoints = "endpoints"
        self.proxy_url = "proxyUrl"
        self.oauth_authorization_endpoint = "oauthAuthorizationEndpoint"
        self.oauth_token_endpoint = "oauthTokenEndpoint"
        self.provide_client_key = "provideClientKey"
        self.sign_client_key = "signClientKey"
        self.shared_inbox = "sharedInbox"
        self.public_key = "publicKey"

    def get_inbox(self) -> Optional[Json]:
        return self.activity_object[self.inbox]

    def get_outbox(self) -> Optional[Json]:
        return self.activity_object[self.outbox]

    def get_following(self) -> Optional[Json]:
        return self.activity_object[self.following]

    def get_followers(self) -> Optional[Json]:
        return self.activity_object[self.followers]

    def get_liked(self) -> Optional[Json]:
        return self.activity_object[self.liked]

    def get_streams(self) -> Optional[Json]:
        return self.activity_object[self.streams]

    def get_preferred_username(self) -> Optional[Json]:
        return self.activity_object[self.preferred_username]

    def get_endpoints(self) -> Optional[Json]:
        return self.activity_object[self.endpoints]

    def get_proxy_url(self) -> Optional[Json]:
        return self.activity_object[self.proxy_url]

    def get_oauth_authorization_endpoint(self) -> Optional[Json]:
        return self.activity_object[self.oauth_authorization_endpoint]

    def get_oauth_token_endpoint(self) -> Optional[Json]:
        return self.activity_object[self.oauth_token_endpoint]

    def get_provide_client_key(self) -> Optional[Json]:
        return self.activity_object[self.provide_client_key]

    def get_sign_client_key(self) -> Optional[Json]:
        return self.activity_object[self.sign_client_key]

    def get_shared_inbox(self) -> Optional[Json]:
        return self.activity_object[self.shared_inbox]

    def get_public_key(self) -> Optional[Json]:
        return self.activity_object[self.public_key]


class Application(Object_):
    def __init__(self, _application: Json) -> None:
        super().__init__(_application)


class Group(Object_):
    def __init__(self, _group: Json) -> None:
        super().__init__(_group)


class Organization(Object_):
    def __init__(self, _organization: Json) -> None:
        super().__init__(_organization)


class Person(Object_):
    def __init__(self, _person: Json) -> None:
        super().__init__(_person)


class Service(Object_):
    def __init__(self, _service: Json) -> None:
        super().__init__(_service)
