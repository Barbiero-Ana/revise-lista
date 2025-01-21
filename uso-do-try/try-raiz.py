'''
4. Implemente uma função que calcule a raiz quadrada de um número fornecido pelo usuário, tratando
entradas inválidas ou números negativos
'''
import math

def raiz(numero):
    raiz = math.sqrt(numero)

    print(f'A √{numero} será = {raiz}')


try:
    print('Seja bem vindo(a) calculadora de raiz quadrada da Cyber\n')
    numero = float(input('Por favor, digite o número que deseja ver a raiz quadrada: '))
    raiz(numero)
except ValueError:
    print('Impossível realizar raiz de número negativo!')

