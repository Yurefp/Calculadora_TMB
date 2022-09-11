'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  -salários até R$ 280,00 (incluindo) : aumento de 20%
  -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  -salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
  -o salário antes do reajuste;
  -o percentual de aumento aplicado;
  -o valor do aumento;
  -o novo salário, após o aumento
'''

sar = input('Digite o falor atual do salario: ')

if(float(sar) < 280):
    paa = 0.2

elif(280 <= float(sar) < 700):
    paa = 0.15

elif(700 <= float(sar) < 1500):
    paa = 0.1

elif(float(sar) >= 1500):
    paa = 0.05

va = float(sar) * float(paa)
saa = float(sar) + float(va)

print('Salario antes do reajuste:', sar)
print('Percentual de aumento aplicado:', float(paa)*100,'%')
print('Valor do aumento:', va)
print('Salario apos o reajuste:', saa)