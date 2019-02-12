from typing import Optional

from project.json_type import Json


class Object_:
    def __init__(self, _object: Json) -> None:
        self.activity_object = _object
        self.properties = ['@context', 'id', 'type', 'attachment', 'attributedTo', 'audience', 'content', 'context',
                           'name', 'endTime', 'generator', 'icon', 'image', 'inReplyTo', 'location', 'preview',
                           'published', 'replies', 'startTime', 'summary', 'source', 'tag', 'updated', 'url', 'to',
                           'bto', 'cc', 'bcc', 'mediaType', 'duration']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.at_context = "@context"
        self.id = "id"
        self.type = "type"
        self.attachment = "attachment"
        self.attributed_to = "attributedTo"
        self.audience = "audience"
        self.content = "content"
        self.context = "context"
        self.name = "name"
        self.end_time = "endTime"
        self.generator = "generator"
        self.icon = "icon"
        self.image = "image"
        self.in_reply_to = "inReplyTo"
        self.location = "location"
        self.preview = "preview"
        self.published = "published"
        self.replies = "replies"
        self.start_time = "startTime"
        self.summary = "summary"
        self.source = "source"
        self.tag = "tag"
        self.updated = "updated"
        self.url = "url"
        self.to = "to"
        self.bto = "bto"
        self.cc = "cc"
        self.bcc = "bcc"
        self.media_type = "mediaType"
        self.duration = "duration"

    def get_at_context(self) -> Optional[Json]:
        return self.activity_object[self.at_context]

    def get_id(self) -> Optional[Json]:
        return self.activity_object[self.id]

    def get_type(self) -> Optional[Json]:
        return self.activity_object[self.type]

    def get_attachment(self) -> Optional[Json]:
        return self.activity_object[self.attachment]

    def get_attributed_to(self) -> Optional[Json]:
        return self.activity_object[self.attributed_to]

    def get_audience(self) -> Optional[Json]:
        return self.activity_object[self.audience]

    def get_content(self) -> Optional[Json]:
        return self.activity_object[self.content]

    def get_context(self) -> Optional[Json]:
        return self.activity_object[self.context]

    def get_name(self) -> Optional[Json]:
        return self.activity_object[self.name]

    def get_end_time(self) -> Optional[Json]:
        return self.activity_object[self.end_time]

    def get_generator(self) -> Optional[Json]:
        return self.activity_object[self.generator]

    def get_icon(self) -> Optional[Json]:
        return self.activity_object[self.icon]

    def get_image(self) -> Optional[Json]:
        return self.activity_object[self.image]

    def get_in_reply_to(self) -> Optional[Json]:
        return self.activity_object[self.in_reply_to]

    def get_location(self) -> Optional[Json]:
        return self.activity_object[self.location]

    def get_preview(self) -> Optional[Json]:
        return self.activity_object[self.preview]

    def get_published(self) -> Optional[Json]:
        return self.activity_object[self.published]

    def get_replies(self) -> Optional[Json]:
        return self.activity_object[self.replies]

    def get_start_time(self) -> Optional[Json]:
        return self.activity_object[self.start_time]

    def get_summary(self) -> Optional[Json]:
        return self.activity_object[self.summary]

    def get_source(self) -> Optional[Json]:
        return self.activity_object[self.source]

    def get_tag(self) -> Optional[Json]:
        return self.activity_object[self.tag]

    def get_updated(self) -> Optional[Json]:
        return self.activity_object[self.updated]

    def get_url(self) -> Optional[Json]:
        return self.activity_object[self.url]

    def get_to(self) -> Optional[Json]:
        return self.activity_object[self.to]

    def get_bto(self) -> Optional[Json]:
        return self.activity_object[self.bto]

    def get_cc(self) -> Optional[Json]:
        return self.activity_object[self.cc]

    def get_bcc(self) -> Optional[Json]:
        return self.activity_object[self.bcc]

    def get_media_type(self) -> Optional[Json]:
        return self.activity_object[self.media_type]

    def get_duration(self) -> Optional[Json]:
        return self.activity_object[self.duration]

    def get_activity_object(self) -> Json:
        # value is not None
        return dict(filter(lambda kv: kv[1] is not None, self.activity_object.items()))


class Link:
    def __init__(self, _link: Json) -> None:
        self.activity_object = _link
        self.properties = ['@context', 'id', 'type', 'href', 'rel', 'mediaType', 'name', 'hreflang', 'height', 'width',
                           'preview']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.at_context = "@context"
        self.id = "id"
        self.type = "type"
        self.href = "href"
        self.rel = "rel"
        self.media_type = "mediaType"
        self.name = "name"
        self.hreflang = "hreflang"
        self.height = "height"
        self.width = "width"
        self.preview = "preview"

    def get_at_context(self) -> Optional[Json]:
        return self.activity_object[self.at_context]

    def get_id(self) -> Optional[Json]:
        return self.activity_object[self.id]

    def get_type(self) -> Optional[Json]:
        return self.activity_object[self.type]

    def get_href(self) -> Optional[Json]:
        return self.activity_object[self.href]

    def get_rel(self) -> Optional[Json]:
        return self.activity_object[self.rel]

    def get_media_type(self) -> Optional[Json]:
        return self.activity_object[self.media_type]

    def get_name(self) -> Optional[Json]:
        return self.activity_object[self.name]

    def get_hreflang(self) -> Optional[Json]:
        return self.activity_object[self.hreflang]

    def get_height(self) -> Optional[Json]:
        return self.activity_object[self.height]

    def get_width(self) -> Optional[Json]:
        return self.activity_object[self.width]

    def get_preview(self) -> Optional[Json]:
        return self.activity_object[self.preview]

    def get_activity_object(self) -> Json:
        # value is not None
        return dict(filter(lambda kv: kv[1] is not None, self.activity_object.items()))


class Activity(Object_):
    def __init__(self, _activity: Json) -> None:
        super().__init__(_activity)
        self.properties = ['actor', 'object', 'target', 'result', 'origin', 'instrument']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.actor = "actor"
        self.object = "object"
        self.target = "target"
        self.result = "result"
        self.origin = "origin"
        self.instrument = "instrument"

    def get_actor(self) -> Optional[Json]:
        return self.activity_object[self.actor]

    def get_object(self) -> Optional[Json]:
        return self.activity_object[self.object]

    def get_target(self) -> Optional[Json]:
        return self.activity_object[self.target]

    def get_result(self) -> Optional[Json]:
        return self.activity_object[self.result]

    def get_origin(self) -> Optional[Json]:
        return self.activity_object[self.origin]

    def get_instrument(self) -> Optional[Json]:
        return self.activity_object[self.instrument]


class IntransitiveActivity:
    def __init__(self, _intransitive_activity: Json) -> None:
        self.activity_object = _intransitive_activity
        self.properties = ['@context', 'id', 'type', 'attachment', 'attributedTo', 'audience', 'content', 'context',
                           'name', 'endTime', 'generator', 'icon', 'image', 'inReplyTo', 'location', 'preview',
                           'published', 'replies', 'startTime', 'source', 'summary', 'tag', 'updated', 'url', 'to',
                           'bto', 'cc', 'bcc', 'mediaType', 'duration', 'actor', 'target', 'result', 'origin',
                           'instrument']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.at_context = "@context"
        self.id = "id"
        self.type = "type"
        self.attachment = "attachment"
        self.attributed_to = "attributedTo"
        self.audience = "audience"
        self.content = "content"
        self.context = "context"
        self.name = "name"
        self.end_time = "endTime"
        self.generator = "generator"
        self.icon = "icon"
        self.image = "image"
        self.in_reply_to = "inReplyTo"
        self.location = "location"
        self.preview = "preview"
        self.published = "published"
        self.replies = "replies"
        self.start_time = "startTime"
        self.source = "source"
        self.summary = "summary"
        self.tag = "tag"
        self.updated = "updated"
        self.url = "url"
        self.to = "to"
        self.bto = "bto"
        self.cc = "cc"
        self.bcc = "bcc"
        self.media_type = "mediaType"
        self.duration = "duration"
        self.actor = "actor"
        self.target = "target"
        self.result = "result"
        self.origin = "origin"
        self.instrument = "instrument"

    def get_at_context(self) -> Optional[Json]:
        return self.activity_object[self.at_context]

    def get_id(self) -> Optional[Json]:
        return self.activity_object[self.id]

    def get_type(self) -> Optional[Json]:
        return self.activity_object[self.type]

    def get_attachment(self) -> Optional[Json]:
        return self.activity_object[self.attachment]

    def get_attributed_to(self) -> Optional[Json]:
        return self.activity_object[self.attributed_to]

    def get_audience(self) -> Optional[Json]:
        return self.activity_object[self.audience]

    def get_content(self) -> Optional[Json]:
        return self.activity_object[self.content]

    def get_context(self) -> Optional[Json]:
        return self.activity_object[self.context]

    def get_name(self) -> Optional[Json]:
        return self.activity_object[self.name]

    def get_end_time(self) -> Optional[Json]:
        return self.activity_object[self.end_time]

    def get_generator(self) -> Optional[Json]:
        return self.activity_object[self.generator]

    def get_icon(self) -> Optional[Json]:
        return self.activity_object[self.icon]

    def get_image(self) -> Optional[Json]:
        return self.activity_object[self.image]

    def get_in_reply_to(self) -> Optional[Json]:
        return self.activity_object[self.in_reply_to]

    def get_location(self) -> Optional[Json]:
        return self.activity_object[self.location]

    def get_preview(self) -> Optional[Json]:
        return self.activity_object[self.preview]

    def get_published(self) -> Optional[Json]:
        return self.activity_object[self.published]

    def get_replies(self) -> Optional[Json]:
        return self.activity_object[self.replies]

    def get_start_time(self) -> Optional[Json]:
        return self.activity_object[self.start_time]

    def get_source(self) -> Optional[Json]:
        return self.activity_object[self.source]

    def get_summary(self) -> Optional[Json]:
        return self.activity_object[self.summary]

    def get_tag(self) -> Optional[Json]:
        return self.activity_object[self.tag]

    def get_updated(self) -> Optional[Json]:
        return self.activity_object[self.updated]

    def get_url(self) -> Optional[Json]:
        return self.activity_object[self.url]

    def get_to(self) -> Optional[Json]:
        return self.activity_object[self.to]

    def get_bto(self) -> Optional[Json]:
        return self.activity_object[self.bto]

    def get_cc(self) -> Optional[Json]:
        return self.activity_object[self.cc]

    def get_bcc(self) -> Optional[Json]:
        return self.activity_object[self.bcc]

    def get_media_type(self) -> Optional[Json]:
        return self.activity_object[self.media_type]

    def get_duration(self) -> Optional[Json]:
        return self.activity_object[self.duration]

    def get_actor(self) -> Optional[Json]:
        return self.activity_object[self.actor]

    def get_target(self) -> Optional[Json]:
        return self.activity_object[self.target]

    def get_result(self) -> Optional[Json]:
        return self.activity_object[self.result]

    def get_origin(self) -> Optional[Json]:
        return self.activity_object[self.origin]

    def get_instrument(self) -> Optional[Json]:
        return self.activity_object[self.instrument]

    def get_activity_object(self) -> Json:
        # value is not None
        return dict(filter(lambda kv: kv[1] is not None, self.activity_object.items()))


class Collection(Object_):
    def __init__(self, _collection: Json) -> None:
        super().__init__(_collection)
        self.properties = ['totalItems', 'current', 'first', 'last', 'items']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.total_items = "totalItems"
        self.current = "current"
        self.first = "first"
        self.last = "last"
        self.items = "items"

    def get_total_items(self) -> Optional[Json]:
        return self.activity_object[self.total_items]

    def get_current(self) -> Optional[Json]:
        return self.activity_object[self.current]

    def get_first(self) -> Optional[Json]:
        return self.activity_object[self.first]

    def get_last(self) -> Optional[Json]:
        return self.activity_object[self.last]

    def get_items(self) -> Optional[Json]:
        return self.activity_object[self.items]


class OrderedCollection(Collection):
    def __init__(self, _ordered_collection: Json) -> None:
        super().__init__(_ordered_collection)


class CollectionPage(Collection):
    def __init__(self, _collection_page: Json) -> None:
        super().__init__(_collection_page)
        self.properties = ['partOf', 'next', 'prev']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.part_of = "partOf"
        self.next = "next"
        self.prev = "prev"

    def get_part_of(self) -> Optional[Json]:
        return self.activity_object[self.part_of]

    def get_next(self) -> Optional[Json]:
        return self.activity_object[self.next]

    def get_prev(self) -> Optional[Json]:
        return self.activity_object[self.prev]


class OrderedCollectionPage(OrderedCollection, CollectionPage):
    def __init__(self, _ordered_collection_page: Json) -> None:
        super().__init__(_ordered_collection_page)
        self.properties = ['startIndex']
        for p in self.properties:
            if p not in self.activity_object:
                self.activity_object[p] = None

        self.start_index = "startIndex"

    def get_start_index(self) -> Optional[Json]:
        return self.activity_object[self.start_index]
