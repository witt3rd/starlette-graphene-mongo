from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp

from database import init_db
from schema import schema

init_db()

routes = [
    Route('/', GraphQLApp(schema=schema))
]

app = Starlette(routes=routes)