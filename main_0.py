from typing import Union

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float


app = FastAPI()


@app.get("/")
def read_root(user_agent: Union[str, None] = Header(None)):
    return {"user_agent": user_agent}


@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key='meucookie', value='123456')
    return {"cookie": True}


@app.get("/get-cookie")
def get_cookie(meucookie: Union[str, None] = Cookie(None)):
    return {"cookie": meucookie}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]
