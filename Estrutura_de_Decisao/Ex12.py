'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  -Salário Bruto até 900 (inclusive) - isento
  -Salário Bruto até 1500 (inclusive) - desconto de 5%
  -Salário Bruto até 2500 (inclusive) - desconto de 10%
  -Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
  Salário Bruto: (5 * 220)        : R$ 1100,00
  (-) IR (5%)                     : R$   55,00  
  (-) INSS ( 10%)                 : R$  110,00
  FGTS (11%)                      : R$  121,00
  Total de descontos              : R$  165,00
  Salário Liquido                 : R$  935,00
'''

rendimento = input('Digite quanto voce ganha por hora trabalhada: ')
hora = input('Digite quantas horas voce trabalhou nesse mes: ')

sb = float(hora) * float(rendimento)

if(float(sb) <900):
    ir = float(sb)*0

elif(900 <= float(sb) < 1500):
    ir = float(sb)*0.05

elif(1500 <= float(sb) < 2500):
    ir = float(sb)*0.10

elif(2500 <= float(sb)):
    ir = float(sb)*0.2

inss = float(sb)*0.1
sindicato = float(sb)*0.03
fgts = float(sb)*0.11

descontos = float(ir)+float(inss)+float(sindicato)
sl = float(sb)-float(descontos)

print('Salario bruto (', hora,'*', rendimento,') \t: R$', sb)
print('(-) IR (', float(ir)*100/float(sb) ,'%) \t\t: R$', ir)
print('(-) INSS (10 %) \t\t: R$', inss)
print('(-) Sindicato (3 %) \t\t: R$', sindicato)
print('FGTS (11 %) \t\t\t: R$', fgts)
print('Total de descontos \t\t: R$', descontos)
print('Salario liquido \t\t: R$', sl)