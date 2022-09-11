'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
  a_ o produto do dobro do primeiro com metade do segundo 
  b_ a soma do triplo do primeiro com o terceiro
  c_ o terceiro elevado ao cubo
'''

def a_(a, b):

    return (float(a)*2) * (float(b)/2)

def b_(a, b):

    return (float(a)*3) + float(b)

def c_(a):

    return float(a)**3

num1 = input('Digite um numero inteiro: ')
num2 = input('Digite outro numero inteiro: ')
num3 = input('Digite um numero real: ')

print('O produto do dobro do primeiro numero com metade do segundo numero eh: ', a_(num1, num2))
print('A soma do triplo do primeiro numero com o terceiro numero eh: ', b_(num1, num3))
print('O terceiro numero elevado ao cubo eh: ', c_(num3))