# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = input('Informe um número: ')
if num.isnumeric() == False:
    exit()
print(f'Analisando o número {num}')
try:
    print('Unidade: ' + num[-1])
except:
    pass
try:
    print('Dezena: ' + num[-2])
except:
    pass
try:
    print('Centena: ' + num[-3])
except:
    pass
try:
    print('Milhar: ' + num[-4])
except:
    pass
