import os
import random
os.system('clear')

print('=====')
print('clase 35- ciclo anidados')
print('=====')
print('\n')


matriz =[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print('====')
print('Mostrando la matriz')
print('====')
print(matriz)
print('\n')
'''
#salida

====
Mostrando la matriz
====
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''


print('====')
print('Mostrando filas "row" y valores individuales "column" ')
print('====')

for row in matriz:
  print(row)
  for column in row:
    print(column)
print('\n')
'''
#salida

====
Mostrando filas "row" y valores individuales "column"
====
[1, 2, 3]
1
2
3
[4, 5, 6]
4
5
6
[7, 8, 9]
7
8
9

'''
