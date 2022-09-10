'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

def media(a, b, c, d):

    return (float(a) + float(b) + float(c) + float(d))/4

nota1 = input('digite a 1º nota: ')
nota2 = input('digite a 2º nota: ')
nota3 = input('digite a 3º nota: ')
nota4 = input('digite a 4º nota: ')

print('A media das notas eh: ', media(nota1, nota2, nota3, nota4,))