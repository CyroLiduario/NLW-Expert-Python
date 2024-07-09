from barcode import Code128
from barcode.writer import ImageWriter
'''
    cria uma classe handler que irá criar um barcode com base no "product_code" informado
'''
class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        '''
            Cria um código de barras do tipo Code128 usando o product_code fornecido e o salva como uma imagem. 
            O caminho onde a imagem foi salva é retornado.
        '''
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'nlw/barcodes/{tag}'
        tag.save(path_from_tag)

        return path_from_tag
