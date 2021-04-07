# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

dis = float(input('Uma distância em metros: '))
print(f'A medida de {dis}m corresponde a')
print(str(dis/1000) + 'km')
print(str(dis/100) + 'hm')
print(str(dis/10) + 'dam')
print('{:.0f}dm'.format(dis*10))
print('{:.0f}cm'.format(dis*100))
print('{:.0f}mm'.format(dis*100))
