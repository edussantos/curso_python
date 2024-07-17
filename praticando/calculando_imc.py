from os import system

nome_user = input('Digite seu nome: ')
peso_user = input('Digite seu peso: ')
altura_user = input('Digite sua altura: ')
system('cls')

try:
    peso_user = peso_user.replace(",", ".")
    altura_user = altura_user.replace(",", ".")
    peso_user = float(peso_user)
    altura_user = float(altura_user)

    imc_user = peso_user / (altura_user**2)

    if imc_user < 18.5:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Magreza')
    elif imc_user <= 24.9:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Peso normal')
    elif imc_user <= 29.9:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Sobrepeso')
    elif imc_user <= 34.9:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Obesidade grau I')
    elif imc_user <= 40:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Obesidade grau II')
    else:
        print(f'Paciente: {nome_user}\nIMC: {imc_user:.2f}\nClassificação: Obesidade grau III')
except:
    print('Valores digitados inválidos!')
