import json


def serializeList(items):
    if not items:
        return None
    return [x.toDict() for x in items]