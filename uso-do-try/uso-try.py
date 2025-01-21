'''
1 - pedir ao usuário que digite um número e trate com exceção caso digite algo que não seja número
'''

print('Olá! Por favor digite um número: ')

try:
    x = float(input('Digite um número: '))
    print(f'O número digitado foi: {x}')

except ValueError:
    print(f'Você não digitou um número válido! Tente novamente')
    
