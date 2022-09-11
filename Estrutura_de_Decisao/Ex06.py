'''Faça um Programa que leia três números e mostre o maior deles'''

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
num3 = input('Digite outro numero: ')

if(float(num1) > float(num2)):
    if(float(num1) > float(num3)):
        print(num1)
    else:
        print(num3)

else:
    if(float(num2) > float(num3)):
        print(num2)
    else:
        print(num3)