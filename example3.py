from starlette.requests import Request
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.routing import Route


LOG_FILE = "./log3.txt"


async def app(scope, receive, send):
    assert scope["type"] == "http"
    request = Request(scope, receive)

    with open(LOG_FILE, "a") as f:
        f.write("\n------------------")
        f.write(repr(scope))
        f.write("\n------------------")
        f.write(repr(receive))
        f.write("\n------------------")
        f.write(repr(send))
        f.write("\n------------------")
        f.write(repr(request.headers))
        f.write("\n------------------")
        f.write(request.headers["host"] + "\n" + request.headers["user-agent"])
        f.write("\n------------------")

    response = JSONResponse({"hello": "world", "x": 1234})
    await response(scope, receive, send)
