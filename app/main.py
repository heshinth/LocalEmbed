from fastapi import FastAPI
from api.router import router

app = FastAPI(
    title="LocalEmbed",
    description="LocalEmbed",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"Project": "LocalEmbed", "description": "LocalEmbed"}


app.include_router(router)
