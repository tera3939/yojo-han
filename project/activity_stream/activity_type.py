from typing import Optional

from project.activity_stream import Activity, IntransitiveActivity
from project.json_type import Json


class Accept(Activity):
    def __init__(self, _accept: Json) -> None:
        super().__init__(_accept)


class TentativeAccept(Accept):
    def __init__(self, _tentative_accept: Json) -> None:
        super().__init__(_tentative_accept)


class Add(Activity):
    def __init__(self, _add: Json) -> None:
        super().__init__(_add)


class Arrive(IntransitiveActivity):
    def __init__(self, _arrive: Json) -> None:
        super().__init__(_arrive)


class Create(Activity):
    def __init__(self, _create: Json) -> None:
        super().__init__(_create)


class Delete(Activity):
    def __init__(self, _delete: Json) -> None:
        super().__init__(_delete)


class Follow(Activity):
    def __init__(self, _follow: Json) -> None:
        super().__init__(_follow)


class Ignore(Activity):
    def __init__(self, _ignore: Json) -> None:
        super().__init__(_ignore)


class Join(Activity):
    def __init__(self, _join: Json) -> None:
        super().__init__(_join)


class Leave(Activity):
    def __init__(self, _leave: Json) -> None:
        super().__init__(_leave)


class Like(Activity):
    def __init__(self, _like: Json) -> None:
        super().__init__(_like)


class Offer(Activity):
    def __init__(self, _offer: Json) -> None:
        super().__init__(_offer)


class Invite(Offer):
    def __init__(self, _invite: Json) -> None:
        super().__init__(_invite)


class Reject(Activity):
    def __init__(self, _reject: Json) -> None:
        super().__init__(_reject)


class TentativeReject(Reject):
    def __init__(self, _tentative_reject: Json) -> None:
        super().__init__(_tentative_reject)


class Remove(Activity):
    def __init__(self, _remove: Json) -> None:
        super().__init__(_remove)


class Undo(Activity):
    def __init__(self, _undo: Json) -> None:
        super().__init__(_undo)


class Update(Activity):
    def __init__(self, _update: Json) -> None:
        super().__init__(_update)


class View(Activity):
    def __init__(self, _view: Json) -> None:
        super().__init__(_view)


class Listen(Activity):
    def __init__(self, _listen: Json) -> None:
        super().__init__(_listen)


class Read(Activity):
    def __init__(self, _read: Json) -> None:
        super().__init__(_read)


class Move(Activity):
    def __init__(self, _move: Json) -> None:
        super().__init__(_move)


class Travel(Activity):
    def __init__(self, _travel: Json) -> None:
        super().__init__(_travel)


class Announce(Activity):
    def __init__(self, _announce: Json) -> None:
        super().__init__(_announce)


class Block(Ignore):
    def __init__(self, _block: Json) -> None:
        super().__init__(_block)


class Flag(Activity):
    def __init__(self, _flag: Json) -> None:
        super().__init__(_flag)


class Dislike(Activity):
    def __init__(self, _dislike: Json) -> None:
        super().__init__(_dislike)


class Question(IntransitiveActivity):
    def __init__(self, _question: Json) -> None:
        super().__init__(_question)
        self.properties = ['oneOf', 'anyOf', 'closed']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.one_of = "oneOf"
        self.any_of = "anyOf"
        self.closed = "closed"

    def get_one_of(self) -> Optional[Json]:
        return self.activity_object[self.one_of]

    def get_any_of(self) -> Optional[Json]:
        return self.activity_object[self.any_of]

    def get_closed(self) -> Optional[Json]:
        return self.activity_object[self.closed]
