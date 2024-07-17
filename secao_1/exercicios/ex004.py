'''
Peça ao usuário para digitar seu nome e idade.
Se o nome e idade forem digitados, exiba:
* O nome do usuário.
* O nome invertido.
* Se o nome contém (ou não) espaços.
* Quantidade de letras do nome.
* A primeira letra do nome.
* A última letra do nome.
Se nada for digitado em nome ou idade, exiba:
'Desculpe, você deixou campos vazios.'
'''
from os import system

nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')
system('cls')

if nome_usuario and idade_usuario:
    print(f'Seu nome é: {nome_usuario}')
    print(f'Seu nome invertido é: {nome_usuario[::-1]}')
    print(f'Sua idade é: {idade_usuario} anos')
    if ' ' in nome_usuario:
        print('Seu nome contém espaços: SIM')
    else:
        print('Seu nome contém espaços: NÃO')
    print(f'Seu nome tem {len(nome_usuario.replace(" ", ""))} letras')
    print(f'A primeira letra do seu nome é: {nome_usuario[0]}')
    print(f'A última letra do seu nome é: {nome_usuario[-1]}')
else:
    print('Desculpe, você deixou campos vazios ou o nome que inseriu foi inválido.')
