'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar.'''

import math

num = input('Digite um numero inteiro: ')

if(math.floor(float(num)) == float(num)):
    if(float(num)%2 == 0):
        print('O numero eh par')
    
    else:
        print('O numero eh impar')

else:
    print('O numero nao eh inteiro')