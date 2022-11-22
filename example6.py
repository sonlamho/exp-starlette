from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from starlette.routing import Route


LOG_FILE = "./log4.txt"


def root(request: Request):
    with open(LOG_FILE, "a") as f:
        f.write("\n------------------")
        f.write(repr(request.headers))
        f.write("\n------------------")
        f.write(repr(request.query_params))
        f.write("\n------------------")

    res_dict = {
        "result": "HELLO ! this is a server response",
        "server sees your query params": dict(request.query_params),
        "server sees your headers": dict(request.headers),
    }

    return JSONResponse(res_dict)  # comment this out to do HTMLResponse below
    return HTMLResponse(
        """
<h1> Hello ! </h1>
<a href=https://www.google.com>google</a>
    """
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/", root),
    ],
)
