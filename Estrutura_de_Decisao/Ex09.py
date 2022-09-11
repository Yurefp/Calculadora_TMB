'''Faça um Programa que leia três números e mostre-os em ordem decrescente'''

num_list = []

for i in range(3):
    num = input('Digite um numero: ')
    num_list.append(num)

num_dec = sorted(num_list, reverse = True)

print(num_dec)