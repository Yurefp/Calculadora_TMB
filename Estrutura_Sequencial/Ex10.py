'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit'''

def convert(c):

    return ((float(c) / 5) * 9) + 32

cel = input('Digite uma temperatura em Celsios: ')

print('A temperatura em Fahrenheit eh: ', convert(cel))