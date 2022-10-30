from datetime import datetime

def min():

    hoje = datetime.now()
    anohj = hoje.year
    meshj = hoje.month

    if(float(meshj) < 10):
        meshj = '0'+meshj

    else:
        print("erro")

    anomin = anohj - 100

    datamin = str(anomin)+'-01'

    return datamin

    
def max():
    hoje = datetime.now()
    anohj = hoje.year
    meshj = hoje.month

    if(float(meshj) < 10):
        meshj = '0'+meshj

    else:
        print("erro")

    datamax = str(anohj)+'-'+str(meshj)

    return datamax

def idade(nasc):
    hoje = datetime.now()
    anonasc = nasc[:4]
    mesnasc = nasc[5:7]
    
    anohj = hoje.year
    meshj = hoje.month

    idade = float(anohj)-float(anonasc)

    dife =  float(meshj) - float(mesnasc)

    if(-6 <= float(dife) < 6):
        idade = idade

    elif(float(dife) > 6):
        idade = float(idade) + 1

    elif(float(dife) < -6):
        idade = float(idade) - 1

    else:
        print("erro")
    
    return idade


