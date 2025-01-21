'''
3. Crie uma função que receba uma lista e retorne o elemento no índice fornecido pelo usuário, tratando
erros como índices fora do alcance ou entradas inválidas.

'''


lista = [2, 5, 6, 76, 34, 45, 74, 33, 23, 221]

def buscar_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return False

try: 
    indice = int(input('Digite o indice: '))
except ValueError:
    print('Erro! Digite um número válido!')

else: 
    elemento = buscar_elemento(lista, indice )
    print(elemento)