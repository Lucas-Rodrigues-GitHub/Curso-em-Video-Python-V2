# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input('Digite seu nome completo: ').split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é ' + n[0].title())
print('Seu último nome é ' + n[-1].title())
