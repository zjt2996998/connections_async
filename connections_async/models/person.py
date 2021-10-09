from tortoise.models import Model
from tortoise import fields


class Person(Model):
    id = fields.IntField(pk=True)
    first_name = fields.TextField(nullable=False)
    last_name = fields.TextField()
    email = fields.CharField(unique=True, nullable=False, max_length=30)
    date_of_birth = fields.DateField(nullable=False)

