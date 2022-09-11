'''Faça um Programa que leia três números e mostre o maior e o menor deles'''

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
num3 = input('Digite outro numero: ')

if(float(num1) > float(num2)):

    if(float(num1) > float(num3)):

        print('Maior numero:', num1)

        if(float(num2) > float(num3)):
            print('Menor numero:', num3)

        else:
            print('Menor numero:', num2)

    else:
        print('Maior numero:', num3)
        print('Menor numero:', num2)

else:

    if(float(num2) > float(num3)):

        print('Maior numero:', num2)

        if(float(num1) > float(num3)):
            print('Menor numero:', num3)

        else:
            print('Menor numero:', num1)

    else:
        print('Maior numero:', num3)
        print('Menor numero:', num1)