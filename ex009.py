# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    if c != 10:
        print(f'{n} x  {c} = {n*c}')
    else:
        print(f'{n} x {c} = {n*c}')
print('-'*12)