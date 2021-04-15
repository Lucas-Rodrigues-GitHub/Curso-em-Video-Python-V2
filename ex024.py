# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = input('Em que cidade você nasceu? ').lower().split()
print('santo' in cid[0])
