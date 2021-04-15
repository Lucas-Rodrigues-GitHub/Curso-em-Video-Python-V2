# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nom = input('Qual é seu nome completo? ').lower()
mod = nom.split()
var = False
for c in mod:
    if c == 'silva':
        var = True
print('Seu nome tem Silva? ' + str(var))
