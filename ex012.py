# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${preço/100*95:.2f}')
