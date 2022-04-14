from starlette.requests import Request
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route


async def app(scope, receive, send):
    assert scope["type"] == "http"
    response = JSONResponse({"hello": "world", "x": 1234})
    await response(scope, receive, send)
