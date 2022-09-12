'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

lado1 = input('Digite o primeiro lado do triangulo: ')
lado2 = input('Digite o segundo lado do triangulo: ')
lado3 = input('Digite o terceiro lado do triangulo: ')

if(float(lado1)<(float(lado2)+float(lado3)) and float(lado2)<(float(lado1)+float(lado3)) and float(lado3)<(float(lado1)+float(lado2))):
    if(float(lado1)==float(lado2) or float(lado1)==float(lado3) or float(lado2)==float(lado3)):
        if(float(lado1)!=float(lado2) or float(lado1)!=float(lado3) or float(lado2)!=float(lado3)):
            print('O triangulo eh isosceles')

        else:
            print('O triangulo eh equilatero')
        
    else:
        print('O triangulo eh escaleno')

else:
    print('Esses valores nao formam um triangulo')
