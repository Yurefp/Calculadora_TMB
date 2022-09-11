'''
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
  Para homens: (72.7*h) - 58
  Para mulheres: (62.1*h) - 44.7
'''

def imc_m(a):

    return (72.7 * float(a)) - 58

def imc_f(a):

    return (62.1 * float(a)) - 44.7

sexo = input('Qual o seu sexo? Digite (m) para masculino ou (f) para feminino ')
altura = input('Digite a sua altura: ')

if(sexo == 'm'):

    print('O peso ideal para um homem da sua altura eh: ', imc_m(altura))

elif(sexo == 'f'):

    print('O peso ideal para uma mulher da sua altura eh: ', imc_f(altura))