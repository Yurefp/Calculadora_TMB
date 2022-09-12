'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia, mes, ano = input('Digite uma data no formato dd/mm/aaaa: ').split('/')

if(1<=float(mes)<=12 and float(dia)>=1):
    if(float(mes)==4 or float(mes)==6 or float(mes)==9 or float(mes)==11):
        if(float(dia) <= 30):
            print('Essa data eh valida')

        else:
            print('Essa data nao eh valida')

    elif(float(mes)==1 or float(mes)==3 or float(mes)==5 or float(mes)==7 or float(mes)==8 or float(mes)==10 or float(mes)==12):
        if(float(dia) <= 31):
            print('Essa data eh valida')

        else:
            print('Essa data nao eh valida')

    elif(float(mes)==2):
        if((float(ano)%4) == 0):
            if(float(dia) <= 29):
                print('Essa data eh valida')

        elif(float(dia) <= 28):
            print('Essa data eh valida')

        else:
            print('Essa data nao eh valida')

else:
    print('Essa data nao eh valida')