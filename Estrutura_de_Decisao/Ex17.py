'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto'''

ano = input('Digite um ano: ')

if((float(ano)%4) == 0):
    print('Esse ano eh bissexto')

else:
    print('Esse ano nao eh bissexto')