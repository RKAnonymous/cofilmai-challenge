import yaml
import functools
import io
from src.apis import apis
from prisma import Prisma
from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()
app.include_router(apis, prefix="/apis")
prisma = Prisma()


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


@app.get("/")
def read_root():
    return {"version": "1.0.0"}


# ./openapi/api.cofilm.yaml creator endpoint
@app.get('/openapi.yaml', include_in_schema=False)
@functools.lru_cache()
def read_openapi_yaml() -> Response:
    openapi_json = app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s)
    return Response(yaml_s.getvalue(), media_type='text/yaml')
