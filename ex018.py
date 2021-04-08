# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {ang} tem o SENO de {cos(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(radians(ang)):.2f}')
