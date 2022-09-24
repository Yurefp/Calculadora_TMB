'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.'''

import math

num = input('Digite um numero: ')

if(math.floor(float(num)) == float(num)):
    print('O numero eh inteiro')

else:
    print('O numero eh decimal')