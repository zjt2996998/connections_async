import os

from quart import Quart
from tortoise.contrib.quart import register_tortoise

from connections_async.views import blueprint


app = Quart(__name__)
app.config.from_object("connections_async.config.Config")
app.register_blueprint(blueprint)

    

@blueprint.route('/')
async def hello():
    return 'hello'


register_tortoise(
        app,
        db_url='mysql://root:very_secure_password@db:3306/dash_hudson_dev',
        modules={"models": [
            'connections_async.models.person',
        ]},
        generate_schemas=False,
    )
