'''
2. Faça um programa que divida dois números fornecidos pelo usuário, tratando erros como divisão por
zero e entrada inválida.

'''


print('Bem vindo(a) a calculadora de divisão!')

try:
    numero = float(input('Digite o número que deseja dividir: '))
    divisor = float(input('Digite o número que será o divisor: '))

    divisao = numero / divisor
    print(f'O resultado da divisão = {numero} / {divisor} = {divisao}')

except ValueError:
    print('Você não digitou um número, tente novamente.')

except ZeroDivisionError:
    print('Erro, divisão por zero não existe. Tente novamente.')