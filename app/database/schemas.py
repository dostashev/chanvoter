from marshmallow import Schema, fields, pprint

class UserSchema(Schema):
    id = fields.Int()
    address = fields.Str()
    private_key = fields.Str()
    coins = fields.Int()


class GirlSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    instagram = fields.Str()
    photo = fields.Str()
    ELO = fields.Float()


class ContestSchema(Schema):
    id = fields.Int()
    first_girl_id = fields.Int()
    first_girl = fields.Nested(GirlSchema)
    second_girl_id = fields.Int()
    second_girl = fields.Nested(GirlSchema)
    begin = fields.DateTime()
    end   = fields.DateTime()
    finalized = fields.Bool()

    class Meta:
        dateformat = '%Y-%m-%dT%H:%M:%S' 
        # for marshmallow 3
        datetimeformat = '%Y-%m-%dT%H:%M:%S'


class VoteSchema(Schema):
    id = fields.Int()
    user_addr = fields.Str()
    user = fields.Nested(UserSchema)
    contest_id = fields.Int()
    contest = fields.Nested(ContestSchema)
    chosen_id = fields.Int()
    

class BetSchema(Schema):
    id = fields.Int()
    coins = fields.Int()
    user_addr = fields.Str()
    user = fields.Nested(UserSchema)
    contest_id = fields.Int()
    contest = fields.Nested(ContestSchema)
    chosen_id = fields.Int()
    finalized = fields.Bool()
    profit = fields.Int(default=0)
