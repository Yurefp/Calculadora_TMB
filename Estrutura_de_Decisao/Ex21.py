'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas
de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo 
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
   -Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
   -Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota 
   de 5 e quatro notas de 1.
'''

import math

saque = input('Digite o valor do saque: ')

if(10 <= float(saque) <= 600): 
    
   cem = math.floor(float(saque)/100)
   cinq = math.floor((float(saque)-cem*100)/50)
   dez = math.floor(((float(saque)-cem*100)-cinq*50)/10)
   cinc = math.floor((((float(saque)-cem*100)-cinq*50)-dez*10)/5)
   um = math.floor((((float(saque)-cem*100)-cinq*50)-dez*10)-cinc*5)

   print(cem, cinq, dez, cinc, um)

   print('Voce deve sacar: ')

   if(float(cem)==0 and float(cinq)==0 and float(dez)==0 and float(cinc)==0 and float(um)!=0):
      print(um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)==0 and float(cinc)!=0 and float(um)==0):
      print(cinc, 'nota(s) de 5 reais')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)==0 and float(cinc)!=0 and float(um)!=0):
      print(cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)!=0 and float(cinc)==0 and float(um)==0):
      print(dez, 'nota(s) de 10 reais')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)!=0 and float(cinc)==0 and float(um)!=0):
      print(dez, 'nota(s) de 10 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)!=0 and float(cinc)!=0 and float(um)==0):
      print(dez, 'nota(s) de 10 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)==0 and float(cinq)==0 and float(dez)!=0 and float(cinc)!=0 and float(um)!=0):
      print(dez, 'nota(s) de 10 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)==0 and float(cinc)==0 and float(um)==0):
      print(cinq, 'nota(s) de 50 reais')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)==0 and float(cinc)==0 and float(um)!=0):
      print(cinq, 'nota(s) de 50 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)==0 and float(cinc)!=0 and float(um)==0):
      print(cinq, 'nota(s) de 50 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)==0 and float(cinc)!=0 and float(um)!=0):
      print(cinq, 'nota(s) de 50 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)==0 and float(um)==0):
      print(cinq, 'nota(s) de 50 reais e', dez, 'nota(s) de 10 reais')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)==0 and float(um)!=0):
      print(cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)!=0 and float(um)==0):
      print(cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)==0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)!=0 and float(um)!=0):
      print(cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)==0 and float(cinc)==0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)==0 and float(cinc)==0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)==0 and float(cinc)!=0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)==0 and float(cinc)!=0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)!=0 and float(cinc)==0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais e', dez, 'nota(s) de 10 reais')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)!=0 and float(cinc)==0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,',dez, 'nota(s) de 10 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)!=0 and float(cinc)!=0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais,',dez, 'nota(s) de 10 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)!=0 and float(cinq)==0 and float(dez)!=0 and float(cinc)!=0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,',dez, 'nota(s) de 10 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)==0 and float(cinc)==0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais e', cinq, 'nota(s) de 50 reais')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)==0 and float(cinc)==0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)==0 and float(cinc)!=0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)==0 and float(cinc)!=0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)==0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais e', dez, 'nota(s) de 10 reais')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)==0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais e', um, 'nota(s) de 1 real')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)!=0 and float(um)==0):
      print(cem, 'nota(s) de 100 reais,',cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais e', cinc, 'nota(s) de 5 reais')

   elif(float(cem)!=0 and float(cinq)!=0 and float(dez)!=0 and float(cinc)!=0 and float(um)!=0):
      print(cem, 'nota(s) de 100 reais,', cinq, 'nota(s) de 50 reais,', dez, 'nota(s) de 10 reais,', cinc, 'nota(s) de 5 reais e', um, 'nota(s) de 1 real')

   