import os
import tiktoken
from dotenv import load_dotenv
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel


load_dotenv()
app = FastAPI()


DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
if not DEFAULT_MODEL:
    raise ImportError


class RequestModel(BaseModel):
    model: str = DEFAULT_MODEL
    text: str


class ResponsModel(BaseModel):
    tokens_count: int


@app.get("/", include_in_schema=False)
def healthcheck():
    return {"status": "ok"}


@app.post("/", response_model=ResponsModel)
def count_tokens(data: RequestModel):
    enc = tiktoken.encoding_for_model(data.model)
    return {"tokens_count": len(enc.encode(data.text))}
