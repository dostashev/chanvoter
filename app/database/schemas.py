from marshmallow import Schema, fields, pprint

class GirlSchema(Schema):
    name = fields.Str()

class hello():
    name = "123"

if __name__ == "__main__":
    gs = GirlSchema()
    h = hello()
    print(gs.dump(h).data)
