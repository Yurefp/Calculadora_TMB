'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''

def area(a):

    return (float(a)**2)*2

lado = input('Digite o tamanho de um dos lados do quadrado: ')

print('O dobro da area do quadrado eh: ', area(lado))