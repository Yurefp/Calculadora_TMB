'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
  a) salário bruto.
  b) quanto pagou ao INSS.
  c) quanto pagou ao sindicato.
  d) o salário líquido.
  e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido
'''

def sl(a, b):
    return float(a)-float(b)

rendimento = input('Digite quanto voce ganha por hora trabalhada: ')
hora = input('Digite quantas horas voce trabalhou nesse mes: ')

sb = float(hora) * float(rendimento)

ir = float(sb)*0.11
inss = float(sb)*0.08
sindicato = float(sb)*0.05

descontos = float(ir)+float(inss)+float(sindicato)

print('Seu salario bruto esse mes foi de: ', sb, 'reais')
print('Voce tera que pagar: ')
print(ir, 'reais de imposto de renda;')
print(inss, 'reais de INSS;')
print(sindicato, 'reais de sindicato')
print('Seu salario liquido esse mes foi de: ', sl(sb, descontos), 'reais')