# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, passa a receber {sal/100*115:.2f}')
