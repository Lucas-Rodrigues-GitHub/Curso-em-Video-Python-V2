# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint
from time import sleep

print('\033[33m-=-\033[m'*20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m'*20)
person = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(3)
computer = randint(0, 5)
if computer != person:
    print(f'\033[31mGANHEI! Eu pensei no número {computer} e não no {person}!\033[m')
else:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
