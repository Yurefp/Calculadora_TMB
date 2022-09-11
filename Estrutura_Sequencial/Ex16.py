'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

met_quad = input('Digite quantos metros quadrados tem a area que voce deseja pitar: ')

def lata(a):
    return math.ceil(float(a)/54)

print('Voce tera que comprar', lata(met_quad), 'latas de tinta por', lata(met_quad)*80, 'reais')