from marshmallow import Schema, fields


class ParticipantSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    picture = fields.String(required=True)
    location = fields.String(required=True)
    about = fields.String(required=True)

