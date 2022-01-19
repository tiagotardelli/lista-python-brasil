while True:
    nome_usuario = input('Digite o nome de usuário: ')
    senha_usuario = input('Digite a senha do usuário: ')
    if nome_usuario == senha_usuario:
        print('Senha do usuário deve ser diferente do nome')
    else:
        print('Senha do usuário válida!')
        break
