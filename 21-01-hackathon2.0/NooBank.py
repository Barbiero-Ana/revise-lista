'''
Hackathon 2.0 de forma mais simples para revisão
'''


'''
        for cliente in clientes:
            if  cpf == cliente['cpf']  and cliente['senha'] == senha_acesso:
                usuario_encontrado = True
                print(f'Acesso confirmado, seja bem-vindo(a), {cliente["nome"]}')
                break 
        if not usuario_encontrado:
            print('Usuário não encontrado ou senha incorreta, tente novamente!\n')
            continue
        break
'''


clientes = [
    {
        'nome' : 'Ana',
        'cpf' : '1234567890',
        'email' : 'ana@gmail.com',
        'saldo' : 5000,
        'senha': '123@455'
    },

    {
        'nome' : 'Carolina',
        'cpf' : '34920482009',
        'email' : 'carolina@gmail.com',
        'saldo' : 8000,
        'senha': '@412355'
    }
]


def verificacao_cpf(cpf):
    for cliente in clientes:
        if cpf == clientes['cpf']:
            return cliente
    return False

def login(cliente, senha):
    if cliente['senha'] == senha:
        return True
    return False


while True:
    print('Bem vindo(a) ao NooBank')
    print('\n1 - Já possuo conta\n2 - Criar conta\n3 - Sair do banco')
    decisao = int(input('Digite a opção que lhe atende - '))

    if decisao == 1:
        #login

        cpf = input('Digite seu CPF (sem os pontos): ') 
        cliente = verificacao_cpf(cpf)
        if cliente:
            senha = input('digite sua senha de acesso: ')
            print(login(cliente, senha))


    elif decisao == 2:
        #criar conta
        print('Seja bem vindo(a) a central de cadastro de usuários')
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF(sem pontos e traços): ')
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua nova senha: ')
        confirm = input('Confirme a senha: ')
        try:
            confirm = input('Digite a senha novamente: ')
            if confirm == senha:
                return True

        except:
            print('A senhas diferem! Tente novamente')
            continue
        
        saldo = float(input('Digite seu atual saldo: '))

        if confirm != senha:
            print('As senhas diferem... Tente novamente.')
            continue

        clientes.append = ({
            'nome' : nome,
            'cpf' : cpf,
            'email': email,
            'senha' : senha,
            'saldo' : saldo
        })

        print('Cliente cadastrado com sucesso! Tente seu login com o cpf e senha informados.')


    
    elif decisao == 3:
        #sair do banco
        print('Saindo do app.. Até a próxima.')
        break

    else:
        print('Opção inválida! Tente novamente.\n')

