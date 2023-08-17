def create_papel_valido():
    return {
        "id": 0,
        "nome": "Teste_papel_valido",
        "sigla": "PAPE12",
        "cnpj": "00000000000001"
    }


def create_papel_invalido(campos_invalido=['sigla']):
    papel_invalido = {
        "id": 0,
        "nome": "Teste_papel_valido",
        "sigla": "PAPE12",
        "cnpj": "00000000000001"
    }
    if 'sigla' in campos_invalido:
        papel_invalido['sigla'] = 'AAAA'
        return papel_invalido
