from datetime import date

from marshmallow import Schema, fields

from connections_async.models.person import Person


TODAY = date.today()


class BaseModelSchema(Schema):

    def __init__(self, strict=True, **kwargs):
        super().__init__(strict=strict, **kwargs)


class PersonSchema(BaseModelSchema):

    id = fields.Integer()
    first_name = fields.Str(
        required=True,
        error_messages={'required': 'missing first name'},
    )
    last_name = fields.Str()
    email = fields.Email(
        required=True,
        error_messages={'required': 'missing email'},
    )
    date_of_birth = fields.Date(
        validate=lambda x: x < TODAY,
        error_messages={'validator_failed': 'Cannot be in the future.'},
    )

    class Meta:
        model = Person