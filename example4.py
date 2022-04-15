from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from datetime import datetime
import orjson


LOG_FILE = "./log4.txt"


def root(request: Request):
    with open(LOG_FILE, "a") as f:
        f.write("\n------------------")
        f.write(repr(request.headers))
        f.write("\n------------------")
        f.write(repr(request.query_params))
        f.write("\n------------------")

    return JSONResponse({"hello": "world", "x": 123123, "now": datetime.now()})


app = Starlette(
    debug=True,
    routes=[
        Route("/", root),
    ],
)
