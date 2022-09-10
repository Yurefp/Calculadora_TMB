'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
'''

def salario(a, b):

    return float(a) * float(b)

rendimento = input('Digite quanto voce ganha por hora trabalhada: ')
hora = input('Digite quantas horas voce trabalhou nesse mes: ')

print('Seu salario esse mes foi de: ', salario(rendimento, hora))