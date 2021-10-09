import os


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "connections_async.models.person",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}


    