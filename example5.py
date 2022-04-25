from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, BackgroundTask
from starlette.routing import Route
from datetime import datetime
import numpy as np
from typing import Any
import orjson


LOG_FILE = "./log5.txt"

OPT = orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY


class MyJSONResponse(Response):
    media_type = "application/json"

    def __init__(
        self,
        content: Any,
        status_code: int = 200,
        headers: dict = None,
        media_type: str = None,
        background: BackgroundTask = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: Any) -> bytes:
        return orjson.dumps(content, option=OPT)


def root(request: Request):
    with open(LOG_FILE, "a") as f:
        f.write("\n------------------")
        f.write(repr(request.headers))
        f.write("\n------------------")
        f.write(repr(request.query_params))
        s = request.query_params._dict
        f.write(str(s))
        f.write("\n------------------")

    return MyJSONResponse(
        {
            "example": 5,
            "x": np.int32(123123),
            "now": datetime.now(),
            "today": datetime.now().date(),
            "arr": np.array([1.3, 5.6, 3.3], dtype="float32"),
        }
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/", root),
    ],
)
