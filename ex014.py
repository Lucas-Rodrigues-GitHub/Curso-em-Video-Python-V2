# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

graus = float(input('Informe a temperatura em °C: '))
fah = graus * 1.8 + 32
print(f'A temperatura de {graus}°C corresponde a {fah}°F!')
