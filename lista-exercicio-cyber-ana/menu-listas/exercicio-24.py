import datetime

compras = {}

while True:
    print('\nSeja bem-vindo ao sistema de compras da CyberEdux\nPor favor, selecione a opção que atende suas vontades...')
    decisao = int(input('\nPor favor, digite:\n1 - Adicionar item à lista de compras\n2 - Remover um item da lista de compras\n3 - Exibir lista de compras\n4 - Sair do sistema\n-   '))

    if decisao == 1:
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o preço do produto: '))
        marca = input('De qual marca é o produto: ')
        validade = input('Digite a validade do produto (formato dd/mm/aaaa): ')

        try:
            data_validade = datetime.datetime.strptime(validade, '%d/%m/%Y')
            validade_formatada = data_validade.strftime('%d/%m/%Y')
        except ValueError:
            print("Formato de data inválido! A data deve estar no formato dd/mm/aaaa.")
            continue

        if nome in compras:
            print('\nEste produto já existe na lista. Atualizando informações de estoque...')
            compras[nome]['quantidade'] += quantidade
        else:
            compras[nome] = {'quantidade': quantidade, 'preco': preco, 'marca': marca, 'validade': validade_formatada}
            print(f'\nO produto {nome} foi adicionado à lista de compras')

    elif decisao == 2:
        print('Qual item deseja remover da lista?')
        remover = input('- ')
        if remover in compras:
            del compras[remover]
            print('\nProduto removido com sucesso!')
        else:
            print('\nProduto não encontrado na lista, tente novamente.')


    elif decisao == 3:
        for chave, valor in compras[nome].items():
            print(f'\n{chave}:{valor}')

    elif decisao == 4:
        print('\nAté uma próxima!')
        break

    else:
        print('\nOpção inválida, tente novamente.')
        continue