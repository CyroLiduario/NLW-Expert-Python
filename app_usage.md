# Introdução
Esse documento irá apresentar brevemente os conceitos abordados no evento NLW Expert assim como o funcionamento da aplicação desenvolvida.

# Setups Iniciais
Os setups iniciais incluíram a crianção dos seguintes arquivos após a criação do virtual environment e instalação das bibliotecas Flask, pylint

- `.gitignore`: define os formatos de arquivos que foram ignorados nos commits.
- `.pylintrc`: define as configurações do pylint, nele pode-se definir erros a serem ignorados pelo pylint setendo a variável disable e listando o código dos erros. Pode ser criado usando o comando ` pylint --generate-rcfile > .pylintrc `
- `.pre-commit-config.yaml`: define algumas configurações do pylint
- `.vscode/settings.json`: define configurações do VS Code, o setup inserido ignora os arquivos pycache.
- A cada nova pasta criada, crie um arquivo `__init__.py` para garantir que as importações entre os módulos funcionem.