'''
26. Ordene uma lista de números em ordem crescente
'''


lista = []

qtd = int(input('Quantos números deseja adicionar a lista: '))

for i in range(qtd):
    numero = int(input(f'digite o valor do {i + 1}ᴼ número: '))
    lista.append(numero)

ordenado = sorted(lista)

print(ordenado)