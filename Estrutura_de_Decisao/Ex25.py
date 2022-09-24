'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   -"Telefonou para a vítima?"
   -"Esteve no local do crime?"
   -"Mora perto da vítima?"
   -"Devia para a vítima?"
   -"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

sus = 0

print('Responda com (s) para sim e (n) para não.')

def p1():
    global sus
    per = input('Telefonou para a vitima? ')

    if(per == 's' or per == 'S'):
        sus = float(sus) + 1

    elif(per == 'n' or per == 'N'):
        sus = sus

    else:
        print('Resposta invalida!')
        return p1()

def p2():
    global sus
    per = input('Esteve no local do crime? ')

    if(per == 's' or per == 'S'):
        sus = float(sus) + 1

    elif(per == 'n' or per == 'N'):
        sus = sus

    else:
        print('Resposta invalida!')
        return p2()

def p3():
    global sus
    per = input('Mora perto da vitima? ')

    if(per == 's' or per == 'S'):
        sus = float(sus) + 1

    elif(per == 'n' or per == 'N'):
        sus = sus

    else:
        print('Resposta invalida!')
        return p3()

def p4():
    global sus
    per = input('Devia para a vitima? ')

    if(per == 's' or per == 'S'):
        sus = float(sus) + 1

    elif(per == 'n' or per == 'N'):
        sus = sus

    else:
        print('Resposta invalida!')
        return p4()

def p5():
    global sus
    per = input('Ja trabalhou com a vitima? ')

    if(per == 's' or per == 'S'):
        sus = float(sus) + 1

    elif(per == 'n' or per == 'N'):
        sus = sus

    else:
        print('Resposta invalida!')
        return p5()

p1()
p2()
p3()
p4()
p5()

if(float(sus) < 2):
    print('Voce eh inocente')
if(float(sus) == 2):
    print('Voce eh suspeito')
if(3 <= float(sus) <= 4):
    print('Voce eh cumplice')
if(float(sus) == 5):
    print('Voce matou a vitima')