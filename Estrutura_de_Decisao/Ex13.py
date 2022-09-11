'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido
'''

dia = input('Digite um dia da semanda de 1 a 7: ')

if(float(dia) == 1):
    print('Domingo')

elif(float(dia) == 2):
    print('Segunda')

elif(float(dia) == 3):
    print('Terca')

elif(float(dia) == 4):
    print('Quarta')

elif(float(dia) == 5):
    print('Quinta')

elif(float(dia) == 6):
    print('Sexta')

elif(float(dia) == 7):
    print('Sabado')

else:
    print('Valor invalido')