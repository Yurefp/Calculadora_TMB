'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso = input('Digite quantos quilos de peixe voce trouxe: ')

def excesso(a):
    return float(a) - 50

def multa(a):
    return float(a) * 4

if(float(peso) <= 50):
    print('A sua carga esta dentro do limite permitido, logo nao tera que pagar multa')

elif(float(peso) > 50):
    print('A sua carga excede o limite em: ', excesso(peso), 'kg')
    print('Sua multa a ser paga eh de: ', multa(excesso(peso)), 'reais')