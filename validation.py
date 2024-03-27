from marshmallow import Schema, fields

class InputSchema(Schema):
    sentence = fields.Str(required=True)