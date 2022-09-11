'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

num1 = input('Digite um numero: ')

if(float(num1)>0):
    print('O valor eh positivo')

elif(float(num1)<0):
    print('O valor eh negativo')

elif(float(num1) == 0):
    print('O valor eh 0')