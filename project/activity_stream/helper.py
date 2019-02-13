import project.activity_stream as act
from project.json_type import Json


def activity_from(obj: Json) -> act.Activity:
    obj_type = obj["type"]
    if obj_type == act.ActivityType.ACTIVITY:
        return act.Activity(obj)
    elif obj_type == act.ActivityType.ACCEPT:
        return act.Accept(obj)
    elif obj_type == act.ActivityType.ADD:
        return act.Add(obj)
    elif obj_type == act.ActivityType.CREATE:
        return act.Create(obj)
    elif obj_type == act.ActivityType.DELETE:
        return act.Delete(obj)
    elif obj_type == act.ActivityType.FOLLOW:
        return act.Follow(obj)
    elif obj_type == act.ActivityType.IGNORE:
        return act.Ignore(obj)
    elif obj_type == act.ActivityType.JOIN:
        return act.Join(obj)
    elif obj_type == act.ActivityType.LEAVE:
        return act.Leave(obj)
    elif obj_type == act.ActivityType.LIKE:
        return act.Like(obj)
    elif obj_type == act.ActivityType.OFFER:
        return act.Offer(obj)
    elif obj_type == act.ActivityType.REJECT:
        return act.Reject(obj)
    elif obj_type == act.ActivityType.REMOVE:
        return act.Remove(obj)
    elif obj_type == act.ActivityType.UNDO:
        return act.Undo(obj)
    elif obj_type == act.ActivityType.UPDATE:
        return act.Update(obj)
    elif obj_type == act.ActivityType.VIEW:
        return act.View(obj)
    elif obj_type == act.ActivityType.LISTEN:
        return act.Listen(obj)
    elif obj_type == act.ActivityType.READ:
        return act.Read(obj)
    elif obj_type == act.ActivityType.MOVE:
        return act.Move(obj)
    elif obj_type == act.ActivityType.TRAVEL:
        return act.Travel(obj)
    elif obj_type == act.ActivityType.ANNOUNCE:
        return act.Announce(obj)
    elif obj_type == act.ActivityType.FLAG:
        return act.Flag(obj)
    elif obj_type == act.ActivityType.DISLIKE:
        return act.Dislike(obj)
    else:
        raise Exception("This is not Activity Object.")


def intransitive_activity_from(obj: Json) -> act.IntransitiveActivity:
    obj_type = obj["type"]
    if obj_type == act.IntransitiveActivityType.INTRANSITIVEACTIVITY:
        return act.IntransitiveActivity(obj)
    elif obj_type == act.IntransitiveActivityType.ARRIVE:
        return act.Arrive(obj)
    elif obj_type == act.IntransitiveActivityType.QUESTION:
        return act.Question(obj)
    else:
        raise Exception("This is not IntransitiveActivity Object.")


def actor_from(obj: Json) -> act.Actor:
    obj_type = obj["type"]
    if obj_type == act.ActorType.ACTOR:
        return act.Actor(obj)
    elif obj_type == act.ActorType.APPLICATION:
        return act.Application(obj)
    elif obj_type == act.ActorType.GROUP:
        return act.Group(obj)
    elif obj_type == act.ActorType.ORGANIZATION:
        return act.Organization(obj)
    elif obj_type == act.ActorType.PERSON:
        return act.Person(obj)
    elif obj_type == act.ActorType.SERVICE:
        return act.Service(obj)
    else:
        raise Exception("This is not Actor Object.")
