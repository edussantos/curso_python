'''
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
from os import system

entrada_usuario = input('Digite um número inteiro: ')
system('cls')

try:
    entrada_usuario = int(entrada_usuario)
    if entrada_usuario % 2 == 0:
        print(f'O número {entrada_usuario} é PAR!')
    else:
        print(f'O número {entrada_usuario} é ÍMPAR!')
except:
    print('VOCÊ NÃO DIGITOU UM NÚMERO INTEIRO')
