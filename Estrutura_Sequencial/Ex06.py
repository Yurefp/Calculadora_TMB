'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

import math

def area(a):

    return math.pi * (float(a)**2)

raio = input('Digite o tamanho do raio da circunferencia: ')

print('O valor da area da circunferencia eh: ', area(raio))