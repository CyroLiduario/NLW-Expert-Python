from typing import Dict

'''
    Esta classe é projetada para representar uma resposta HTTP, contendo um código de status e um corpo de resposta.
'''
class HttpResponse:
    def __init__(self, status_code: int, body: Dict) -> None:
        # Um inteiro (int) que representa o código de status HTTP
        self.status_code = status_code

        # Um dicionário que contém o corpo da resposta, geralmente representado em formato JSON.
        self.body = body
