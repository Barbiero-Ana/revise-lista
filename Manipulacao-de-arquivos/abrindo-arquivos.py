'''
exercicio 1 
- crie um arquivo
- Escreva as novas frases no texto
- leia os arquivos e os imprima na tela
'''

with open ('arquivo_ana.txt','w') as arquivo:
    arquivo.write('\nTestando a função de escrita dentro do python\nE vamos de contúdo novo :D\n')
    arquivo.writelines(['linha 1\n','linha 2\n'])
    


with open ('arquivo_ana.txt', 'r') as arquivo:
    print(arquivo.read())

# Readline lê linha por linha