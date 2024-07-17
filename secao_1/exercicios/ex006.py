'''
Faça um programa que pergunte a hora ao usuário.
Baseando-se no horário descrito, exiba a saudação apropriada.
Ex.: Bom dia se a hora for entre 0-11, Boa tarde se a hora for entre 12-17 e Boa noite se a hora for entre 18-23.
'''
from os import system

hora_entrada_usuario = input(
    'Digite a hora atual em números inteiros (SOMENTE AS HORAS): ')
system('cls')

try:
    hora_entrada_usuario = int(hora_entrada_usuario)

    if hora_entrada_usuario >= 0 and hora_entrada_usuario <= 11:
        print('Bom dia!')
    elif hora_entrada_usuario >= 12 and hora_entrada_usuario <= 17:
        print('Boa tarde!')
    elif hora_entrada_usuario >= 18 and hora_entrada_usuario <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora :(')
except:
    print('[ERRO] - Não foi digitado números inteiros ou não foi digitado nenhum valor.')
