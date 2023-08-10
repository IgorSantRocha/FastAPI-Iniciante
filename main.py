from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    descricao: str
    valor: float


app = FastAPI()

banco_de_dados = []


@app.post("/item")
def add_item(item: Item):
    banco_de_dados.append(item)
    return item


@app.get("/item")
def list_item():
    return banco_de_dados


@app.get("/item/valor_total")
def get_valor_total():
    valor_total = 0.0
    for item in banco_de_dados:
        valor_total = item.valor * item.quantidade
    return {"valor_total": valor_total}
