'''
2. Use `map()` com uma função lambda para converter uma lista de temperaturas de Celsius para
Fahrenheit.
'''

temp_celcius = [22, 35, 40, 32, 20, 10, 46]

temp_f = list(map(lambda c: (c * 9/5) + 32, temp_celcius))

print(temp_f)
print(temp_celcius)