from unidecode import unidecode
from base.base_dados import livros


def tratar_string(string):
    string = str(string)
    return unidecode(string.lower())


def gerando_lista_autores():
    lista_autores = []
    for livro in livros:
        lista_autores.append(tratar_string(livros[livro]['autor']))
    return lista_autores


def gerando_lista_livros():
    lista_livros = []
    for livro in livros:
        lista_livros.append(tratar_string(livro))
    return lista_livros
