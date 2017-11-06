import json


def serializeList(items):
    if not items:
        return None
    return [x.toJSON() for x in items]