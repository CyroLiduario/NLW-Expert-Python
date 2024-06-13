from typing import Dict

'''
    Define a classe HttpRequest que irá representar as requisições HTTP da aplicação
'''

class HttpRequest:
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
