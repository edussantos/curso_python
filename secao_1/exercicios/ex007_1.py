'''
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva "Seu nome é curto".
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal".
Maior que 6 escreva "Seu nome é muito grande". 
'''
from os import system

nome_usuario = input('Digite seu primeiro nome: ')
system('cls')

if len(nome_usuario) <= 4:
    print(
        f'Quantidade de letras do nome: {len(nome_usuario)}\nSeu nome é curto!')
elif len(nome_usuario) >= 5 and len(nome_usuario) <= 6:
    print(
        f'Quantidade de letras do nome: {len(nome_usuario)}\nSeu nome tem um tamanho normal!')
else:
    print(
        f'Quantidade de letras do nome: {len(nome_usuario)}\nSeu nome é muito grande!')
