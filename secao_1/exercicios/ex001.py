'''
Faça o trexo de código abaixo funcionar, utilizando os conceitos de variáveis e tipos de dados.
print('Nome', nome)<br>
print('Sobrenome', sobrenome)<br>
print('Idade', idade)<br>
print('Ano de nascimento', ano_nascimento)<br>
print('É maior de idade?', maior_de_idade)<br>
print('Altura em metros', altura_metros)
'''
from datetime import datetime

nome = 'Eduardo'
sobrenome = 'Santos'
idade = 22
ano_nascimento = datetime.now().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.84

print(f'Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade} anos\nAno de nascimento: {ano_nascimento}\nÉ maior de idade: {maior_de_idade}\nAltura em metros: {altura_metros}')
