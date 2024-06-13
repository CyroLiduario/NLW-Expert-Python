from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

'''
    Cria o server em flask e registra o blueprint
    Adicionando à aplicação principal as rotas relacionadas a ele
'''

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)
