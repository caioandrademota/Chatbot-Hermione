# imports
from flask import Flask, render_template, request
from unidecode import unidecode

app = Flask(__name__,  template_folder='.', static_folder='page')


# tira acentuacao e deixa minusculo
def tratar_string(string):
    return unidecode(string.lower())


def menu(msg):
    msg = tratar_string(msg)
    # livro epecifico
    if msg == '1' or msg in "buscar informacoes de um livro especifico":
        return 'Informe o livro que deseja pesquisar: '
    return 'Preciso de melhorias!'

# define app routes


@app.route("/")
def index():
    return render_template("page/index.html")


@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return menu(userText)


if __name__ == "__main__":
    app.run()
