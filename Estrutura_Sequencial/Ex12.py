'''
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

def imc(a):

    return (72.7 * float(a)) - 58

altura = input('Digite a altura de uma pessoa: ')

print('O peso ideal para essa pessoa eh: ', imc(altura))