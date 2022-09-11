'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input('Digite (F) para feminino e (M) para masculino: ')

if(letra == 'f' or letra == 'F'):
    print('Feminino')

elif(letra == 'm' or letra == 'M'):
    print('Masculino')

else:
    print('Sexo invalido')