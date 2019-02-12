from enum import Enum
from project.activity_stream import Activity, Actor


class ActivityType(Enum):
    ACCEPT = "Accept"
    TENTATIVE_ACCEPT = "TentativeAccept"
    ADD = "Add"
    ARRIVE = "Arrive"
    CREATE = "Create"
    DELETE = "Delete"
    FOLLOW = "Follow"
    IGNORE = "Ignore"
    JOIN = "Join"
    LEAVE = "Leave"
    LIKE = "Like"
    OFFER = "Offer"
    INVITE = "Invite"
    REJECT = "Reject"
    TENTATIVE_REJECT = "TentativeReject"
    REMOVE = "Remove"
    UNDO = "Undo"
    UPDATE = "Update"
    VIEW = "View"
    LISTEN = "Listen"
    READ = "Read"
    MOVE = "Move"
    TRAVEL = "Travel"
    ANNOUNCE = "Announce"
    BLOCK = "Block"
    FLAG = "Flag"
    DISLIKE = "Dislike"
    QUESTION = "Question"

    def __eq__(self, other) -> bool:
        if isinstance(other, Activity):
            return self.value == other.get_type()
        return False


class ActorType(Enum):
    APPLICATION = "Application"
    GROUP = "Group"
    ORGANIZATION = "Organization"
    PERSON = "Person"
    SERVICE = "Service"

    def __eq__(self, other) -> bool:
        if isinstance(other, Actor):
            return self.value == other.get_type()
        return False
