'''Faça um Programa que converta metros para centímetros.'''

def convert(a):

    return float(a)*100

metro = input('Digite um valor em metros: ')

print(metro ,'metros equivale a:',convert(metro),'cm')