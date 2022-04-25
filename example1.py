from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"hello": "world", "x": 123123, "example": 1})


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
    ],
)
