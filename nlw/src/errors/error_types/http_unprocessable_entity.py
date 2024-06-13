class HttpUnprocessableEntityError(Exception):
    '''
        Define a exceção personalizada HttpUnprocessableEntityError para representar um erro HTTP 422 (Unprocessable Entity)
    '''
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
