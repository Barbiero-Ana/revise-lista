'''
27. Filtre números pares de uma lista
'''

lista = []

qtd = int(input('Quantos números deseja adicionar a lista: '))

for i in range(qtd):
    numero = int(input(f'digite o valor do {i + 1}ᴼ número: '))
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        print(f'os números pares são: {numero}')

    else:
        print(f'não há números pares.')