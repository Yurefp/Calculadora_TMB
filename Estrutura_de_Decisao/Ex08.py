'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''

prod1, prec1 = input('Digite o nome do primeiro produto e seu preco: ').split()
prod2, prec2 = input('Digite o nome do segundo e seu preco: ').split()
prod3, prec3 = input('Digite o nome do terceiro e seu preco: ').split()

if(float(prec1) < float(prec2)):
    if(float(prec1) < float(prec3)):
        print('Voce deve comprar:', prod1)
    else:
        print('Voce deve comprar:', prod3)

else:
    if(float(prec2) < float(prec3)):
        print('Voce deve comprar:', prod2)
    else:
        print('Voce deve comprar:', prod3)