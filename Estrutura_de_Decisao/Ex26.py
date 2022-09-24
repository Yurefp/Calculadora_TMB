'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
       -até 20 litros, desconto de 3% por litro
       -acima de 20 litros, desconto de 5% por litro
    Gasolina:
       -até 20 litros, desconto de 4% por litro
       -acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do 
álcool é R$ 1,90.
'''

def p1():
    comb = input('Com o que voce deseja abastecer? \nDigite (A) para alcool e (G) para gasolina: ')

    if(comb == 'a' or comb == 'A'):
        l = input('Quantos litros deseja colocar? ')
        p = float(l) * 1.9

        if(float(l) <= 20):
            p = float(p) * 0.97
        elif(float(l) > 20):
            p = float(p) * 0.95

    elif(comb == 'g' or comb == 'G'):
        l = input('Quantos litros deseja colocar? ')
        p = float(l) * 2.5

        if(float(l) <= 20):
            p = float(p) * 0.94
        elif(float(l) > 20):
            p = float(p) * 0.94
    
    else:
        print('Tipo de combostivel nao reconhecido!')
        return p1()

    print('O valor a ser pago eh de R$', p)

p1()
     
