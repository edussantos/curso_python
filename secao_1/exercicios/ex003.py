'''
Leia dois números do usuário e verifique qual é o maior e qual é o menor e 
Verifique também se eles são iguais.
'''
from os import system

primeiro_valor = input('Digite um valor inteiro: ')
segundo_valor = input('Digite outro valor inteiro: ')
system('cls')

try:
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)

    if primeiro_valor > segundo_valor:
        print(
            f'Os valores digitados foram:\nPrimeiro valor -> {primeiro_valor}\nSegundo valor -> {segundo_valor}\nO primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).')
    elif primeiro_valor < segundo_valor:
        print(
            f'Os valores digitados foram:\nPrimeiro valor -> {primeiro_valor}\nSegundo valor -> {segundo_valor}\nO segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor}).')
    else:
        print(
            f'Os valores digitados foram:\nPrimeiro valor -> {primeiro_valor}\nSegundo valor -> {segundo_valor}\nOs valores são iguais! ({primeiro_valor} = {segundo_valor})')
except:
    print('Valores digitados inválidos! Digite valores numéricos inteiros.')
