import os
from base_dados import livros
from base_dados import livros_precos
from unidecode import unidecode


# tira acentuacao e deixa minusculo
def tratar_string(string):
    return unidecode(string.lower())


def definindo_genero(genero_escolhido):
    genero_tratado = tratar_string(genero_escolhido)

    if genero_tratado == '1' or "romance" in genero_tratado:
        return 'Romance'
    elif genero_tratado == '2' or "ficcao" in genero_tratado:
        return 'Ficção'
    elif genero_tratado == '3' or "fantasia" in genero_tratado:
        return 'Fantasia'
    elif genero_tratado == '4' or "anime" in genero_tratado:
        return 'Anime'
    elif genero_tratado == '5' or "financas" in genero_tratado:
        return 'Finanças'
    elif genero_tratado == '6' or "religiao" in genero_tratado:
        return 'Religião'
    elif genero_tratado == '7' or "misterio" in genero_tratado:
        return 'Misterio'
    elif genero_tratado == '8' or "manga hq" in genero_tratado or "hq" in genero_tratado or "manga" in genero_tratado or "hqs" in genero_tratado:
        return 'Mangá HQs'
    elif genero_tratado == '9' or "psicanalise" in genero_tratado:
        return 'Psicanalise'
    elif genero_tratado == '10' or "autoajuda" in genero_tratado:
        return 'Autoajuda'
    elif genero_tratado == '11' or "infantil" in genero_tratado:
        return 'Infantil'
    else:
        print("não entendi :(")
        return ''


# def listagem_generos():
#     generos = []
#     i = 1
#     for livro in livros:
#         if tratar_string(livros[livro]['genero']) not in generos:
#             generos.append(tratar_string(livros[livro]['genero']))
#             i += 1
#     return generos


def pesquisar_livro(nome_livro):
    nome_tratado = tratar_string(nome_livro)

    for livro in livros:
        if nome_tratado in tratar_string(livro):
            print('nome -', livro)
            for k, v in livros[livro].items():
                print(k, "-", v)


def pesquisar_genero(genero):
    genero = definindo_genero(genero)
    print('Resultados para o gênero: ', genero)

    genero_tratado = tratar_string(genero)

    for livro in livros:
        if tratar_string(livros[livro]['genero']) == genero_tratado:
            print(livro)


def pesquisar_autor(nome_autor):
    nome_tratado = tratar_string(nome_autor)

    for livro in livros:
        if nome_tratado in tratar_string(livros[livro]['autor']):
            print(livro)


def pesquisar_avaliacao():
    for livro in livros:
        if int(livros[livro]['posicao']) < 11:
            print(livro)


def pesquisar_preco():
    i = 1
    for livro, preco in livros_precos.items():
        print(f'{i} - {livro}')
        print(f'preço: {preco}\n')
        i += 1


def menu(resposta):
    resposta_tratada = tratar_string(resposta)

    # livro epecifico
    if resposta == '1' or resposta_tratada in "buscar informacoes de um livro especifico":
        os.system("cls")

        nome_livro = input('Informe o livro que deseja pesquisar: ')
        pesquisar_livro(nome_livro)

    # indicações por gênero
    elif resposta == '2' or resposta_tratada in "indicacoes de livros por genero":
        os.system("cls")

        genero_escolhido = input(
            'Selecione um gênero:\n[1] Romance\n[2] Ficção\n[3] Fantasia\n[4] Anime\n[5] Finanças\n[6] Religião\n[7] Misterio\n[8] Mangá HQs\n[9] Psicanalise\n[10] Autoajuda\n[11] Infantil\n')

        pesquisar_genero(genero_escolhido)

    # indicações por autor
    elif resposta == '3' or resposta_tratada in "indicacoes de livros por autor":
        os.system("cls")

        autor_escolhido = input('Informe o autor que deseja pesquisar: ')
        pesquisar_autor(autor_escolhido)

    # indicações por melhor classificação
    elif resposta == '4' or resposta_tratada in "indicacoes de livros por melhor classificacao":
        os.system("cls")
        pesquisar_avaliacao()

    # indicações por preço
    # elif resposta == '5' or resposta_tratada in "indicacoes de livros por preco":

    else:
        print("não entendi :(")


def start():
    # apresentar chatbot
    print('\nola! me chamo Hermione\n')

    # oferecer menu de possibilidades
    resposta = input(
        'o que você deseja saber?\n[1] Buscar informações de um livro especifico\n[2] Indicações de livros por gênero\n[3] Indicações de livros por autor\n[4] Indicaçoes de livros por melhor classificação\n[5] Indicaçoes de livros por preço\n\n')

    # processar as respostas
    menu(resposta)


if __name__ == '__main__':
    start()
