# Teste unitário do tag_creator_controller
from unittest.mock import patch
# patch do módulo unittest.mock: 
# Usado para substituir temporariamente o método create_barcode por um mock.

from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

''' 
    o decorador @patch.object substitui os atributos de um projeto por um mock value para teste
    o parâmetro mock_create_barcode é criado a partir desse decorador
'''
@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    '''
        realiza o teste da função create_barcode com um valor mock de product_code
    '''
    mock_value = "image_path"
    mock_create_barcode.return_value = mock_value
    tag_creator_controler = TagCreatorController()

    result = tag_creator_controler.create(mock_value)

    print()
    print(result)

    '''
        As asserções abaixo verificam se o resultado está formatado corretamente conforme esperado.
    '''
    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'
