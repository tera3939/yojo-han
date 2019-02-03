from enum import Enum


class ActivityType(Enum):
    FOLLOW = "Follow"
    UNDO = "Undo"

    def __eq__(self, other):
        return self.value == other
