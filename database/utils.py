def serialize(obj, load_relations=True):
    res = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    if load_relations:
        for c in obj.__mapper__.relationships.keys():
            res[c] = serialize(getattr(obj, c))
    return res
