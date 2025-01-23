'''
1. - Contar palavras: Leia o conteúdo de um arquivo e conte o número total de palavras.
2. - Número de linhas: Crie um script que conta e exibe o número total de linhas em um arquivo.
3. - Copia e cola: Leia um arquivo e copie seu conteúdo para outro arquivo chamado copia.txt.
4. - Busca em arquivos: Leia um arquivo e procure por uma palavra específica. Exiba as linhas onde a
palavra aparece.
5. - Ordenar palavras: Leia o conteúdo de um arquivo, extraia todas as palavras, e salve-as em ordem
alfabética em um novo arquivo
6. - Remoção de linhas vazias: Leia um arquivo e crie outro arquivo sem linhas em branco.
7. - Estatísticas do texto: Leia um arquivo e exiba:
* O número total de caracteres.
* O número de palavras.
* O número de linhas.

'''
#LEMBRETE* o arquivo de texto precisa estar fora da mesma pasta que o código para que consiga ser buscada
#LEMBRETE* para adicionar o texto no final do arquivo, é preciso usar o metôdo append 'a'
#LEMBRETE* ESTUDE OS COMANDOS DE ARQUIVO
#Comando 'seek' - faz com que o arquivo volte para o inicio

import re

while True:
    
    print('\n1 - digitar algo novo no arquivo\n2 - ver quantidade de palavras no arquivo\n3 - Abrir arquivo\n4 - Ver quantidade total de linhas do arquivo\n5 - copiar e colar o arquivo para outro arquivo\n6 - Busca dentro do arquivo\n7 - Ordenar as palavras presentes no arquivo\n8 - Remoção de linhas vazias presentes no arquivo e passar para outro\n9 - Estatistica do arquivo\n10 - sair')
    decisao = int(input('- '))

    if decisao == 1:
        new_text = input('Digite o que deseja adicionar ao arquivo de texto: ')
        with open('arquivo_ana.txt', 'a') as arquivo:
            arquivo.write(new_text + '\n')
            decision = int(input('Deseja adicionar mais algumas linhas ao código? 1 - sim/ 2 - não\n-'))
            if decision == 1:
                while True:
                    print('\nSe deseja sair digite 3')
                    linha = input('Digite a linha que deseja adicionar ao arquivo de texto: ')
                    if linha == '3':
                        break
                    arquivo.write(linha + '\n')
            elif decision == 2:
                break

    elif decisao == 2:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                conteudo = arquivo.read() 
                palavras = conteudo.split()  
                quantidade = len(palavras)  
                print(f'\nQuantidade total de palavras: {quantidade}')
        except FileNotFoundError:
            print('Erro! Arquivo não encontrado.')

    elif decisao == 3:
        print('Qual arquivo você deseja ver?\n1 - "arquivo_ana.txt"\n2 - "cópia"\n3 - "arquivo_alfabético.txt"\n4 - "arquivo_vazio.txt" ')
        opt = int(input('Digite a opção que deseja: '))

        if opt == 1: 
            try:
                with open('arquivo_ana.txt', 'r') as arquivo:
                    print(f'\n{arquivo.read()}')
            except FileNotFoundError:
                print('Arquivo não encontrado.')

        elif opt == 2:
            try:
                with open('novo_copia_ana.txt', 'r') as arquivo:
                    print(f'\n{arquivo.read()}') 
            except FileNotFoundError:
                print('Arquivo não encontrado.')

        elif opt == 3:
            try: 
                with open('arquivo_alfabetico.txt', 'r') as arquivo:
                    print(f'\n{arquivo.read()}')
            except FileNotFoundError:
                print('Arquivo não encontrado.')

        elif opt == 4:
            try: 
                with open('arquivo_vazio.txt', 'r') as arquivo:
                    print(f'\n{arquivo.read()}')
            except FileNotFoundError:
                print('Arquivo não encontrado.')

    elif decisao == 4:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                linhas = arquivo.readlines() 
                print(f'Quantidade total de linhas no arquivo: {len(linhas)}') 
        except FileNotFoundError:
            print('O arquivo não existe no diretório')

    elif decisao == 5:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                conteudo = arquivo.read()

            with open('novo_copia_ana.txt', 'w') as arquivo:
                arquivo.write(conteudo)
            print('Arquivo copiado com sucesso!')
        except FileNotFoundError:
            print('Erro! Arquivo não encontrado.')

    elif decisao == 6:
        filtro = input('Digite o que deseja buscar no arquivo: ')

        try: 
            with open('arquivo_ana.txt', 'r') as arquivo:
                linhas = arquivo.readlines() 
                encontrou = filter(lambda linha: filtro.lower() in linha.lower(), linhas)
                encontrou = list(encontrou)
                if encontrou: 
                    for n_linha, linha in enumerate(encontrou, 1): 
                        print(f'Linha {n_linha}: {linha.strip()}')
                else:
                    print(f'A palavra "{filtro}" não foi encontrada.') 
        except FileNotFoundError:
            print('Arquivo não encontrado')

    elif decisao == 7:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                palavras = conteudo.split()
                palavras = [re.sub(r'[^\w\s]', '', palavra) for palavra in palavras] 
                palavras.sort()

            with open('arquivo_alfabetico.txt', 'w') as arquivo_alfabetico:
                for palavra in palavras:
                    arquivo_alfabetico.write(palavra + '\n')
            print('Processo realizado com sucesso.')
        except FileNotFoundError:
            print('Erro! Arquivo não encontrado.')

    elif decisao == 8:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                linhas = arquivo.readlines() 
            linha_vazio = [linha for linha in linhas if linha.strip() != '']  
            
            with open('arquivo_vazio.txt', 'w') as arquivo_vazio:
                for linha in linha_vazio:
                    arquivo_vazio.write(linha)
            print('Espaços vazios removidos.')
        except FileNotFoundError:
            print('Erro! Arquivo não encontrado.')

    elif decisao == 9:
        try:
            with open('arquivo_ana.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                num_linhas = len(linhas)

                cont_palavras = 0
                cont_caracteres = 0

                for linha in linhas:
                    palavras = linha.split()
                    cont_palavras += len(palavras)
                    cont_caracteres += len(linha)

                print(f'O número total de caracteres é de: {cont_caracteres}')
                print(f'O número total de palavras é de: {cont_palavras}')
                print(f'O número total de linhas é de: {num_linhas}')
        except FileNotFoundError:
            print('Erro! Arquivo não encontrado.')

    elif decisao == 10:
        print('Saindo do sistema...')
        break

    else: 
        print('Opção inválida, tente novamente')



'''
total = len('arquivo_ana.txt')

print(total)
'''