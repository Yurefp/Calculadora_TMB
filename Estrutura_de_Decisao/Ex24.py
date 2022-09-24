'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
   -par ou ímpar;
   -positivo ou negativo;
   -inteiro ou decimal.
'''

import math

num1 = input('Digite o valor de n1: ')
num2 = input('Digite o valor de n2: ')

op = input('Qual operação deseja realizar? \n(+) para soma \n(-) para soma \n(/) para soma \n(*) para soma \n')

if(op == '+'):
    res = float(num1) + float(num2)

if(op == '-'):
    res = float(num1) - float(num2)

if(op == '/'):
    res = float(num1) / float(num2)

if(op == '*'):
    res = float(num1) * float(num2)



if(math.floor(float(res)) == float(res)):
    inde = 'inteiro'
    
    if(float(res)%2 == 0):
        paim = 'par'
    else:
        paim = 'impar'

else:
    inde = 'decimal'

    arre = res
    while(math.floor(float(arre)) != float(arre)):
        arre = float(arre)*10

    if(float(arre)%2 == 0):
        paim = 'par'
    else:
        paim = 'impar'


if(float(res) >= 0):
    pone = 'positivo'
else:
    pone = 'negativo'


print('O resultado de', num1,op,num2, 'eh:', res, ',', paim, ',', pone, 'e', inde)