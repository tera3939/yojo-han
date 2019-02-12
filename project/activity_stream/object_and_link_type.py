from typing import Optional

from project.activity_stream import Object_, Link
from project.json_type import Json


class Relationship(Object_):
    def __init__(self, _relationship: Json) -> None:
        super().__init__(_relationship)
        self.properties = ['subject', 'object', 'relationship']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.subject = "subject"
        self.object = "object"
        self.relationship = "relationship"

    def get_subject(self) -> Optional[Json]:
        return self.activity_object[self.subject]

    def get_object(self) -> Optional[Json]:
        return self.activity_object[self.object]

    def get_relationship(self) -> Optional[Json]:
        return self.activity_object[self.relationship]


class Article(Object_):
    def __init__(self, _article: Json) -> None:
        super().__init__(_article)


class Document(Object_):
    def __init__(self, _document: Json) -> None:
        super().__init__(_document)


class Audio(Document):
    def __init__(self, _audio: Json) -> None:
        super().__init__(_audio)


class Image(Document):
    def __init__(self, _image: Json) -> None:
        super().__init__(_image)


class Video(Document):
    def __init__(self, _video: Json) -> None:
        super().__init__(_video)


class Note(Document):
    def __init__(self, _note: Json) -> None:
        super().__init__(_note)


class Page(Document):
    def __init__(self, _page: Json) -> None:
        super().__init__(_page)


class Event(Document):
    def __init__(self, _event: Json) -> None:
        super().__init__(_event)


class Place(Document):
    def __init__(self, _place: Json) -> None:
        super().__init__(_place)
        self.properties = ['accuracy', 'altitude', 'latitude', 'longitude', 'radius', 'units']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.accuracy = "accuracy"
        self.altitude = "altitude"
        self.latitude = "latitude"
        self.longitude = "longitude"
        self.radius = "radius"
        self.units = "units"

    def get_accuracy(self) -> Optional[Json]:
        return self.activity_object[self.accuracy]

    def get_altitude(self) -> Optional[Json]:
        return self.activity_object[self.altitude]

    def get_latitude(self) -> Optional[Json]:
        return self.activity_object[self.latitude]

    def get_longitude(self) -> Optional[Json]:
        return self.activity_object[self.longitude]

    def get_radius(self) -> Optional[Json]:
        return self.activity_object[self.radius]

    def get_units(self) -> Optional[Json]:
        return self.activity_object[self.units]


class Mention(Link):
    def __init__(self, _mention: Json) -> None:
        super().__init__(_mention)


class Profile(Object_):
    def __init__(self, _profile: Json) -> None:
        super().__init__(_profile)
        self.properties = ['describes']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.describes = "describes"

    def get_describes(self) -> Optional[Json]:
        return self.activity_object[self.describes]


class Tombstone(Object_):
    def __init__(self, _tombstone: Json) -> None:
        super().__init__(_tombstone)
        self.properties = ['formerType', 'deleted']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.former_type = "formerType"
        self.deleted = "deleted"

    def get_former_type(self) -> Optional[Json]:
        return self.activity_object[self.former_type]

    def get_deleted(self) -> Optional[Json]:
        return self.activity_object[self.deleted]
