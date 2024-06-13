from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
        responsability for creating business rules
    '''

    def create(self, product_code: str) -> Dict:
        '''
            Este método coordena o processo de criação da tag do produto. 
            Ele chama os métodos privados __create_tag e __format_response.
        '''
        path_from_tag = self.__create_tag(product_code)
        formated_response = self.__format_response(path_from_tag)
        return formated_response

    def __create_tag(self, product_code: str) -> str:
        '''
            Cria um handler de código de barras (BarcodeHandler).
            Utiliza o método create_barcode do handler para gerar um código de barras baseado no product_code.
        '''
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        '''
            Formata a resposta em um dicionário contendo os detalhes da tag criada.
        '''
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
