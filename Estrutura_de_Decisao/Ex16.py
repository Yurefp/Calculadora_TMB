'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os 
valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
  a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais 
     valores, sendo encerrado;
  b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
  c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
  d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

def baskara(a, b, c):

    d = float(b)**2 - 4*float(a)*float(c)

    x1 = (-float(b)-(float(d)**(1/2)))/(2*float(a))
    x2 = (-float(b)+(float(d)**(1/2)))/(2*float(a))

    if(float(d) < 0):
        print('Essa funcao nao possui raizes')

    elif(float(d) == 0):
        print('Essa funcao possui apenas uma raiz, sendo ela:', x1) 

    else:
        print('Essa funcao possui duas raiz, sendo elas:', x1,',', x2) 


print('Tendo o modelo de uma funcao do 2º grau: ax2 + bx + c')
a = input('Digite o valor de a: ')

if(float(a) == 0):
    print('Essa nao pode mais ser uma funcao do 2º grau')

else:
    b = input('Digite o valor de b: ')
    c = input('Digite o valor de c: ')

    baskara(a, b, c)

