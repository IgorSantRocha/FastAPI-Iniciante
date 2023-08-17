from fastapi import APIRouter, Response
from models.papel import Papel
from models.requests.papel_update import PapelUpdate
from ormar import exceptions

router = APIRouter()


@router.post("/")
async def add_item(papel: Papel):
    await papel.save()
    return papel


@router.get("/")
async def list_item():
    return await Papel.objects.all()


@router.get("/{papel_id}")
async def get_papel(papel_id: int, response: Response):
    try:
        papel = await Papel.objects.get(id=papel_id)
        return papel
    except exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada"}


@router.patch("/{papel_id}")
async def patch_papel(propiedades_atualizacao: PapelUpdate, papel_id: int,
                      response: Response):
    try:
        papel_salvo = await Papel.objects.get(id=papel_id)
        propiedades_atualizadas = propiedades_atualizacao.dict(
            exclude_unset=True)
        await papel_salvo.update(**propiedades_atualizadas)
        return papel_salvo
    except exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada"}


@router.delete("/{papel_id}")
async def delete_papel(papel_id: int, response: Response):
    try:
        papel = await Papel.objects.get(id=papel_id)
        return await papel.delete()
    except exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada"}
