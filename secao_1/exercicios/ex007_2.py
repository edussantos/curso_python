from os import system

nome_usuario = input('Digite seu primeiro nome: ')
system('cls')

nome_curto = len(nome_usuario) <= 4
nome_normal = len(nome_usuario) >= 5 and len(nome_usuario) <= 6
nome_grande = len(nome_usuario) > 6

if ' ' in nome_usuario:
    print('Voce digitou um nome composto ou somente espaços! :(')
elif len(nome_usuario) >= 3:
    if nome_curto:
        print(
            f'Seu nome é curto! Ele possui {len(nome_usuario)} letras.')
    elif nome_normal:
        print(
            f'Seu nome é de tamanho normal! Ele possui {len(nome_usuario)} letras.')
    elif nome_grande:
        print(
            f'Seu nome é muito grande! Ele possui {len(nome_usuario)} letras.')
else:
    print('Nome muito curto :(\nDigite um nome com pelo menos 3 letras!')
