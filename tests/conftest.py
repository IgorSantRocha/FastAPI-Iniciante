import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from cria_tabelas import configurar_banco
from main import app
import pytest
from fastapi.testclient import TestClient
from typing import Generator


# foo bar baz


@pytest.fixture(scope="function")
def client() -> Generator:
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c
