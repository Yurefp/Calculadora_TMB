'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
  -A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
  -A mensagem "Reprovado", se a média for menor do que sete;
  -A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1 = input('Digite o valor da 1º nota: ')
nota2 = input('Digite o valor da 2º nota: ')

media = (float(nota1) + float(nota2))/2

if(float(media)==10):
    print('Aprovado com Distinção')

elif(float(media)<10 and float(media)>=7):
    print('Aprovado')

elif(float(media)<7):
    print('Reprovado')