from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

'''
    Faz a validação do formato do request com base no schema fornecido em body_validator
'''

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": {
            "type": "string", "required": True, "empty": False
        }
    })

    response = body_validator.validate(request.json)
    if response is False:
        # Se o request for inválido, o erro de UnprocessedEntity será indicado
        raise HttpUnprocessableEntityError(body_validator.errors)
