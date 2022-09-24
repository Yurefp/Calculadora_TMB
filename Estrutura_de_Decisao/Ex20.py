'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
   -A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
   -A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
   -A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')

media = (float(nota1) + float(nota2) + float(nota3))/3

if(7 <= float(media) < 10):
    print('Aprovado')

elif(float(media) < 7):
    print('Reprovado')

elif(float(media) == 10):
    print('Aprovado com Distinção')
