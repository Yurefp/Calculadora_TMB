'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
  -326 = 3 centenas, 2 dezenas e 6 unidades
  -12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

import math

num = input('Digite um numero inteiro menor que 1000: ')

if(float(num) < 1000):

    if(float(num)<0):
        num = float(num)*(-1)

    cent = math.floor(float(num)/100)
    dez = math.floor((float(num)-(float(cent)*100))/10)
    uni = math.floor(float(num)-(float(cent)*100)-(float(dez)*10))

    if(float(uni) == 1):
        val_uni = 'unidade'

    elif(float(uni) != 1):
        val_uni = 'unidades'

    if(float(dez) == 1):
        val_dez = 'dezena'

    elif(float(dez) != 1):
        val_dez = 'dezenas'

    if(float(cent) == 1):
        val_cent = 'centena'

    elif(float(cent) != 1):
        val_cent = 'centenas'

    if(float(cent) == 0 and float(dez) == 0):
        print(uni, val_uni)

    elif(float(cent) == 0 and float(dez) != 0 and float(uni) == 0):
        print(dez, val_dez)

    elif(float(cent) != 0 and float(dez) == 0 and float(uni) == 0):
        print(cent, val_cent)

    elif(float(cent) == 0 and float(dez) != 0 and float(uni) != 0):
        print(dez, val_dez, 'e', uni, val_uni)

    elif(float(cent) != 0 and float(dez) != 0 and float(uni) == 0):
        print(cent, val_cent, 'e', dez, val_dez)

    elif(float(cent) != 0 and float(dez) == 0 and float(uni) != 0):
        print(cent, val_cent, 'e', uni, val_uni)

    elif(float(cent) != 0 and float(dez) != 0 and float(uni) != 0):
        print(cent, val_cent, ',', dez, val_dez, 'e', uni, val_uni)
    

else:
    print('Esse numero nao eh valido')