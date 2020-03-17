from marshmallow import Schema, fields


class ParticipantSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    picture = fields.String(required=True)
    location = fields.String(required=True)
    about = fields.String(required=True)


class LocationSchema(Schema):
    id = fields.Integer(dump_only=True)
    code = fields.String(required=True)
    title = fields.String(required=True)


class EventTypeSchema(Schema):
    id = fields.Integer(dump_only=True)
    code = fields.String(required=True)
    title = fields.String(required=True)


class EventCategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    code = fields.String(required=True)
    title = fields.String(required=True)


class EventSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.Date(required=True)
    time = fields.Time(required=True)
    seats = fields.Integer(required=True)
    address = fields.String()
    type = fields.Nested('EventTypeSchema')
    locations = fields.List(fields.Nested('LocationSchema'))
    categories = fields.List(fields.Nested('EventCategorySchema'))
