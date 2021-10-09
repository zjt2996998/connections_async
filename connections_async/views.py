from http import HTTPStatus

from quart import Blueprint, jsonify, request
from webargs import asyncparser
from marshmallow import ValidationError
from connections_async.models.person import Person
from connections_async.schemas import PersonSchema



blueprint = Blueprint('connections', __name__)
parser = asyncparser.AsyncParser()

@blueprint.route('/people', methods=['GET'])
async def get_people():
    people_schema = PersonSchema(many=True)
    people = await Person.all()
    return jsonify(people_schema.dump(people)), HTTPStatus.OK


@blueprint.route('/people', methods=['POST'])
async def create_person():
    try:
        data = await request.get_json()
        data = PersonSchema().load(data).data
        person = Person(**data)
        await person.save()
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    return jsonify(PersonSchema().dump(person)), HTTPStatus.CREATED
