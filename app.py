# -*- coding: utf-8 -*-
import os

# lista de livros
Livros={'torto arado':{'paginas':'264','autor': 'Itamar Vieira','genero': 'Ficção', 'editora': 'todavia', 'preco': '36,9', 'avaliacao': '4,8', 'data': '07/08/2019', 'posicao': '1', 'sinopse': 'Nas profundezas do sertão baiano, as irmãs Bibiana e Belonísia encontram uma velha e misteriosa faca na mala guardada sob a cama da avó. Ocorre então um acidente. E para sempre suas vidas estarão ligadas ― a ponto de uma precisar ser a voz da outra. Numa trama conduzida com maestria e com uma prosa melodiosa, o romance conta uma história de vida e morte, de combate e redenção.' }}

def resposta_genero(resposta):
    if resposta=='1':
        genero='Romance'
    if resposta=='2':
        genero='Ficçao'
    if resposta=='3':
        genero='Fantasia'
    if resposta=='4':
        genero='Literatura'
    if resposta=='5':
        genero='Finanças'
    if resposta=='6':
        genero='Religião'
    if resposta=='7':
        genero='Misterio'
    if resposta=='8':
        genero='Mangá HQ'
    if resposta=='9':
        genero='Psicologia'
    if resposta=='10':
        genero='Autoajuda'
    if resposta=='11':
        genero='Infantil'
    if resposta=='12':
        genero='Politica'
    
   
    

def resposta_start(resposta):
    if resposta == 1:
        resposta= input('Informe o livro que deseja pesquisar: ')
    if resposta == 2:
        resposta = input('Selecione um gênero:\n[1] Romance\n[2] Ficção\n[3] Fantasia\n[4] Literatura\n[5] Finanças\n[6] Religião\n[7] Misterio\n[8] Mangá HQs\n[9] Psicologia\n[10] Autoajuda\n[11] Infantil\n[12] Politica\n')
        resposta_genero(resposta)
    if resposta == 3:
        resposta= input('Informe o Autor que deseja pesquisar: ')
    if resposta == 4:
        respostra= input
    #else resposta == '5':
    #    pass

def start():
    #apresentar chatbot
    print('ola! me chamo Hermione\n')
    #oferecer menu de possibilidades
    resposta= input('\no que você deseja saber?\n[1]Buscar informações de um livro especifico\n[2] Indicações de livros por gênero\n[3] Indicações de livros por autor\n[5] Indicaçoes de livros por preço\n')
    #processar as respostas
    
    resposta_start(resposta)


if __name__ == '__main__':
    start()
