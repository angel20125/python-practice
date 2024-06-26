import os
import random
os.system('clear')

'''
En este desafío, se te proporcionará una lista de números llamada my_list. Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. Luego, debes agregar estos números a una nueva lista llamada new_list. Al final del ciclo, debes imprimir los valores contenidos en new_list utilizando la función print.

Por ejemplo, si la lista es [1, -1, 2, -2, 3, -3, 4, -4], después de realizar las operaciones descritas, la lista new_list debería contener solo los números positivos, es decir, [1, 2, 3, 4].

Input: [1, -1, 2, -2, 3, -3, 4, -4]
Output: [1, 2, 3, 4]
'''

print('=====')
print('clase 34- ciclo anidados')
print('=====')
print('\n')


my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇

for value in my_list:
  if value > 0:
    new_list.append(value)

print(new_list)

'''
#salida

python3 34-reto-ciclo.py
[1, 2, 3, 4]
'''
