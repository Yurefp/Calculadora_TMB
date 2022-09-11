'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:    
   -comprar apenas latas de 18 litros;
   -comprar apenas galões de 3,6 litros;
   -misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
    os valores para cima, isto é, considere latas cheias.
'''

import math

met_quad = input('Digite quantos metros quadrados tem a area que voce deseja pitar: ')

def lata(a):
    return math.ceil(float(a)/(18*6))

def galao(a):
    return math.ceil(float(a)/(3.6*6))

litros = math.ceil(float(met_quad)/6)
latas = math.floor(litros/18)
galoes = math.ceil((litros-(latas*18))/3.6)

print('Voce tera que comprar:')
print(lata(met_quad), 'latas por', lata(met_quad)*80, 'reais;')
print(galao(met_quad), 'galoes por', galao(met_quad)*25, 'reais;')
print(latas, 'latas por', latas*80, 'reais e', galoes, 'galoes por', galoes*25, 'reais;')