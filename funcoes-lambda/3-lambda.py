'''
3. Utilize `filter()` com uma função lambda para obter todos os números pares de uma lista.
'''

lista = list(range(21))

lista_par = list(filter(lambda x: x % 2 == 0, lista))

print(lista_par)