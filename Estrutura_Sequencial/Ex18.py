'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

arquivo = input('Digite o tamanho do arquivo em MB: ')
velocidade = input('Digite a velocidade da internet em Mbps: ')

def tempo(a, v):
    return ((float(a)*8)/float(v))/60

print('Ira levar', tempo(arquivo, velocidade), 'minutos')