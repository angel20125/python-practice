import os
import random
os.system('clear')

print('\n')
print('=====')
print('Clase 12 return python')
print('=====')
print('\n')

print('Crear una función que reciba como parámetros dos números (min, max) y luego realize un suma sucesiva desde el elemento minímo hasta el elemento máximo ejemplo: la funcion recibe min:10 hasta max:20')
print('\n')

def sum_with_range(min, max):
  print('valores mínimo y máximo', min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result = sum_with_range(1, 10)
print(result)
result = sum_with_range(10, 20)
print(result)


'''
#salida

valores mínimo y máximo 1 10
45
valores mínimo y máximo 10 20
145
'''
