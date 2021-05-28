import os
from base_dados import livros


def pesquisar_genero(genero_escolhido):
    if genero_escolhido == '1':
        return 'Romance'
    elif genero_escolhido == '2':
        return 'Ficçao'
    elif genero_escolhido == '3':
        return 'Fantasia'
    elif genero_escolhido == '4':
        return 'Literatura'
    elif genero_escolhido == '5':
        return 'Finanças'
    elif genero_escolhido == '6':
        return 'Religião'
    elif genero_escolhido == '7':
        return 'Misterio'
    elif genero_escolhido == '8':
        return 'Mangá HQ'
    elif genero_escolhido == '9':
        return 'Psicologia'
    elif genero_escolhido == '10':
        return 'Autoajuda'
    elif genero_escolhido == '11':
        return 'Infantil'
    elif genero_escolhido == '12':
        return 'Politica'


def pesquisar_livro(nome_livro):
    print('vou pesquisar...')
    # desenvolver...


def pesquisar_autor(nome_autor):
    print('vou pesquisar...')
    # desenvolver...


def pesquisar_preco(preco_livro):
    print('vou pesquisar...')
    # desenvolver...


def menu(resposta):

    if resposta == 1:
        nome_livro = input('Informe o livro que deseja pesquisar: ')
        pesquisar_livro(nome_livro)

    elif resposta == 2:
        genero_escolhido = input(
            'Selecione um gênero:\n[1] Romance\n[2] Ficção\n[3] Fantasia\n[4] Literatura\n[5] Finanças\n[6] Religião\n[7] Misterio\n[8] Mangá HQs\n[9] Psicologia\n[10] Autoajuda\n[11] Infantil\n[12] Politica\n')
        pesquisar_genero(int(genero_escolhido))

    elif resposta == 3:
        resposta = input('Informe o Autor que deseja pesquisar: ')

    # elif resposta == 4:
    #     respostra = input
    # else resposta == '5':
    #    pass


def start():
    # apresentar chatbot
    print('\nola! me chamo Hermione\n')
    # oferecer menu de possibilidades
    resposta = input(
        'o que você deseja saber?\n[1] Buscar informações de um livro especifico\n[2] Indicações de livros por gênero\n[3] Indicações de livros por autor\n[5] Indicaçoes de livros por preço\n')
    # processar as respostas

    menu(int(resposta))


if __name__ == '__main__':
    start()
