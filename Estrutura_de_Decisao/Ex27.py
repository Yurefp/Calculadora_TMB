'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto 
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
'''

mo = input('Quantos Kg de morango deseja comprar? ')
ma = input('Quantos Kg de maca deseja comprar? ')

if(float(mo) <= 5):
    pmo = 2.5
elif(float(mo) > 5):
    pmo = 2.2

if(float(ma) <= 5):
    pma = 1.8
elif(float(ma) > 5):
    pma = 1.5

pt = float(pma)*float(ma) + float(pmo)*float(mo)

if(float(float(ma)+float(mo)) > 8 or float(pt) > 25):
    pt = float(pt) * 0.9
    print('O valor a ser pago eh R$', pt)

else:
    print('O valor a ser pago eh R$', pt)