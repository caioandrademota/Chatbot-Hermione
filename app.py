# imports
from flask import Flask, render_template, request, jsonify
from unidecode import unidecode
from werkzeug.utils import redirect

from base.base_dados import livros
from base.base_dados import livros_precos
from base.base_dados import lista_generos

from base.tratamento_dados import gerando_lista_autores
from base.tratamento_dados import gerando_lista_livros
from base.tratamento_dados import tratar_string


app = Flask(__name__, static_url_path='',
            static_folder='page', template_folder='page')

lista_autores = gerando_lista_autores()
lista_livros = gerando_lista_livros()


def pesquisar_genero(genero):
    string_livros = f'Resultados para o gênero {genero}: <br>'

    for livro in livros:
        if tratar_string(livros[livro]['genero']) == genero:
            string_livros += f"- {livro}<br>"

    return string_livros


def pesquisar_autor(autor):
    lista_livros_autor = ''

    for livro in livros:
        if autor in tratar_string(livros[livro]['autor']):
            lista_livros_autor += f'- {livro}<br>'

    if lista_livros_autor:
        return jsonify({"resp": lista_livros_autor, 'extra': 'Para saber mais sobre algum desses livros, insira o nome dele!'})


def pesquisar_livro(livro_parametro):
    info_livro = ''

    for livro in livros:
        if livro_parametro in tratar_string(livro):
            info_livro = f'''Nome do livro: {livro}<br>
                            {livros[livro]["paginas"]} paginas<br>
                            Autor(a): {livros[livro]["autor"]}<br>
                            Gênero do livro: {livros[livro]["genero"]}<br>
                            Preço: R$ {livros[livro]["preco"]}<br>
                            Editora: {livros[livro]["editora"]}<br>
                            Avaliação: {livros[livro]["avaliacao"]}/5.0<br>
                            Data de publicação do livro: {livros[livro]["data"]}<br>
                            Sinopse: <i>{livros[livro]["sinopse"]}</i>'''

    if info_livro:
        return jsonify({"resp": info_livro, 'extra': 'Posso te ajudar em algo mais?'})


def pesquisar_avaliacao():
    string_livros = ''
    i = 1
    for livro in livros:
        try:
            if int(livros[livro]['posicao']) < 11:
                string_livros += f'#{i}- {livro}<br>'
            i += 1
        except():
            pass
    return string_livros


def pesquisar_preco():
    string_livros = ''

    for livro, preco in livros_precos.items():
        string_livros += f'- {livro} - R${preco}<br>'

    return string_livros


def confere_genero(msg):
    for genero in lista_generos:
        if genero in msg:
            return genero
    return False


def confere_autor(msg):
    for autor in lista_autores:
        if autor in msg:
            return autor
    return False


def confere_livro(msg):
    for livro in lista_livros:
        if livro in msg:
            return livro
    return False


def menu(msg):
    resposta_tratada = tratar_string(msg)

    genero = confere_genero(resposta_tratada)
    autor = confere_autor(resposta_tratada)
    livro = confere_livro(resposta_tratada)

    # confere se a mensagem contem algum livro especifico
    if resposta_tratada == '1':
        return redirect('/pesquisar_livro')

    # indicações por genero
    elif resposta_tratada == '2':
        return redirect('/pesquisar_genero')

    # indicações por autor
    elif resposta_tratada == '3':
        return redirect('/pesquisar_autor')

    # indicações por melhor classificação
    elif resposta_tratada == '4':
        return redirect('/pesquisar_avaliacao')

    # indicações por melhores precos
    elif resposta_tratada == '5':
        return redirect('/pesquisar_precos')

    # confere se a mensagem contem algum dos generos da lista
    elif genero:
        path = f'/pesquisar_genero/{genero}'
        return redirect(path)

    # confere se a mensagem contem algum dos generos da lista
    elif autor:
        path = f'/pesquisar_autor/{autor}'
        return redirect(path)

    # confere se a mensagem contem algum dos livros da lista
    elif livro:
        path = f'/pesquisar_livro/{livro}'
        return redirect(path)

    elif 'menu' in resposta_tratada or 'inici' in resposta_tratada:
        return redirect('/menu')

    elif 'nao' in resposta_tratada:
        return jsonify({"resp": "Tudo bem! Me chame sempre que precisar :)", 'extra': None})

    elif 'tchau' in resposta_tratada:
        return jsonify({"resp": "Tchau, querido leitor! Volte sempre :)", 'extra': None})

    else:
        return jsonify({"resp": "Poxa :( não consigo te ajudar com isso!", 'extra': 'Posso te ajudar com outra coisa?'})


# define app routes
@ app.route("/")
def index():
    return render_template("index.html")


@ app.route("/pesquisar_livro")
@ app.route("/pesquisar_livro/<livro>")
def index_livro(livro=None):
    if livro:
        return pesquisar_livro(livro)
    else:
        redirect('/pesquisar_livro/')
        return jsonify({"resp": "Informe o nome do livro:", 'extra': None})


@ app.route("/pesquisar_genero")
@ app.route("/pesquisar_genero/<genero>")
def index_genero(genero=None):
    if genero:
        return jsonify({"resp": pesquisar_genero(genero), "extra": 'Para saber mais sobre algum desses livros, insira o nome dele!'})
    else:
        redirect('/pesquisar_genero/')
        return jsonify({"resp": '''Romance<br>
                                Ficção<br>
                                Fantasia<br>
                                Anime<br>
                                Finanças<br>
                                Religião<br>
                                Misterio<br>
                                Mangá HQs<br>
                                Psicanalise<br>
                                Autoajuda<br>
                                Infantil<br>''',
                        'extra': 'Sobre qual gênero você deseja pesquisar?'})


@ app.route("/pesquisar_autor")
@ app.route("/pesquisar_autor/<autor>")
def index_autor(autor=None):
    if autor:
        return pesquisar_autor(autor)
    else:
        redirect('/pesquisar_autor/')
        return jsonify({"resp": "Informe o nome do autor:", 'extra': None})


@ app.route("/pesquisar_avaliacao")
def index_avaliacao():
    return jsonify({"resp": pesquisar_avaliacao(), 'extra': 'Para saber mais sobre algum desses livros, insira o nome dele!'})


@ app.route("/pesquisar_precos")
def index_precos():
    return jsonify({"resp": pesquisar_preco(), 'extra': 'Para saber mais sobre algum desses livros, insira o nome dele!'})


@ app.route("/menu")
def index_menu():
    return jsonify({"resp": '''[1] Buscar informações de um livro específico<br>
                            [2] Indicações por gênero<br>
                            [3] Indicações por autor<br>
                            [4] Indicações por boa avaliação<br>
                            [5] Indicações de melhores preços<br>''',
                    'extra': None})


@ app.route("/get")
# function for the bot response
def get_bot_response():
    msg = request.args.get('msg')
    return menu(msg)


if __name__ == "__main__":
    app.run()
