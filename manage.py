from quart.cli import QuartGroup
from connections_async.app import app

cli = QuartGroup(app)

if __name__ == "__main__":
    cli()