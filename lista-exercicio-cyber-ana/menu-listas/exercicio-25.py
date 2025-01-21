'''
25. Encontre o maior e menor número em uma lista

'''

lista = []

# A funções max e min - pegam o máximo e o minimo dentro de uma lista - max(argument) - min(argument)

while True:
    print('\nSeja bem vindo(a) a lista da cyberedux! Selecione a opção que deseja:\n')
    print('1 - Adicionar números a lista\n2 - Encontrar números da lista\n3 - Sair')
    decisao = int(input('- '))

    if decisao == 1:
        qtd = int(input('Quantos números deseja adicionar a lista: '))
        for i in range(qtd):
            numero = int(input(f'Digite o {i + 1}°valor a ser adicionado a lista: '))
            lista.append(numero)
    elif decisao == 2:
        print('O que deseja fazer?')
        opt = int(input('1 - Encontrar o menor número na lista\n2 - Econtrar o maior número na lista\n- '))
        if opt == 1:
            menor = min(lista)
            print(f'O menor número da lista é: {menor}')
        elif opt == 2:
            maior = max(lista)
            print(f'O maior número dentro da lista é: {maior}')

    elif decisao == 3:
        print('Saindo do sistema, até uma próxima.')
        break


    else:
        print('Opção inválida, tente...')