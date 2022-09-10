'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius'''

def convert(f):

    return 5 * ((float(f) - 32) / 9)

fah = input('Digite uma temperatura em Fahrenheit: ')

print('A temperatura em Celsios eh: ', convert(fah))