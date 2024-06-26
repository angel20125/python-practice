import os
import functools
os.system('clear')
print('\n')
print('=====')
print('Clase 25 función reduce')
print('=====')

'''
resumen

La función reduce() en Python es una función incorporada que se utiliza
para aplicar una función en particular a la lista de elementos de
manera sucesiva. Esta función se define en el módulo functools.

import functools

En este ejemplo, reduce() toma la función suma y la lista lista como
argumentos. Aplica la función suma de manera sucesiva a los elementos
de la lista de tal manera que solo queda un solo valor al final.
'''




numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter  => :',counter)
  print('item     => :',item)
  print('counter + item=> : ',counter + item)

  print('\n')
  return counter + item

result = functools.reduce(accum, numbers)

print('result',result)

'''
#salida

counter  => : 1
item     => : 2
counter + item=> :  3


counter  => : 3
item     => : 3
counter + item=> :  6


counter  => : 6
item     => : 4
counter + item=> :  10


result 10

'''
