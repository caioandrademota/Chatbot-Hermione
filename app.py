import os
from base_dados import livros


def resposta_genero(resposta):
    if resposta == '1':
        return 'Romance'
    elif resposta == '2':
        return 'Ficçao'
    elif resposta == '3':
        return 'Fantasia'
    elif resposta == '4':
        return 'Literatura'
    elif resposta == '5':
        return 'Finanças'
    elif resposta == '6':
        return 'Religião'
    elif resposta == '7':
        return 'Misterio'
    elif resposta == '8':
        return 'Mangá HQ'
    elif resposta == '9':
        return 'Psicologia'
    elif resposta == '10':
        return 'Autoajuda'
    elif resposta == '11':
        return 'Infantil'
    elif resposta == '12':
        return 'Politica'


def resposta_start(resposta):
    if resposta == 1:
        resposta = input('Informe o livro que deseja pesquisar: ')
    elif resposta == 2:
        resposta = input(
            'Selecione um gênero:\n[1] Romance\n[2] Ficção\n[3] Fantasia\n[4] Literatura\n[5] Finanças\n[6] Religião\n[7] Misterio\n[8] Mangá HQs\n[9] Psicologia\n[10] Autoajuda\n[11] Infantil\n[12] Politica\n')
        resposta_genero(resposta)
    elif resposta == 3:
        resposta = input('Informe o Autor que deseja pesquisar: ')
    # elif resposta == 4:
    #     respostra = input
    # else resposta == '5':
    #    pass


def start():
    # apresentar chatbot
    print('ola! me chamo Hermione\n')
    # oferecer menu de possibilidades
    resposta = input(
        '\no que você deseja saber?\n[1]Buscar informações de um livro especifico\n[2] Indicações de livros por gênero\n[3] Indicações de livros por autor\n[5] Indicaçoes de livros por preço\n')
    # processar as respostas

    resposta_start(int(resposta))


if __name__ == '__main__':
    start()
