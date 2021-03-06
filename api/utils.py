import json
from api.models import PointsOfInterest, AdditionalLinks, Content

def serializeList(items):
    if not items or items is None:
        return []
    return [x.toDict() for x in items]

def serializePOI(items):
    if not items:
        return []
    ret_list = []
    for elm in items:
        poi_id = elm.id
        dict2 = elm.toDict()
        dict2["additional_links"] = serializeList(AdditionalLinks.query.filter(AdditionalLinks.poi_id==poi_id))
        dict2["content"] = serializeList((Content.query.filter(Content.poi_id==poi_id)))
        ret_list.append(dict2)
    return ret_list
