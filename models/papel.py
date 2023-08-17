import ormar
import re
from pydantic import validator
from config import database, metadata


class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'papeis'

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=14)

    @validator('sigla')
    def valida_formatacao_sigla(cls, v):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):
            raise ValueError('A sigla adicionada para o papel é inválida!')
        return v
