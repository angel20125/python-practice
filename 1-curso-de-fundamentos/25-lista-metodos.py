import os
import random
os.system('clear')

print('=====')
print('clase 25: Métodos de Lista')
print('=====')
print('\n')


list_number = [1,2,3,5]
list_task = ['work','study','play']

print('====')
print('Leer de un lista')
print('====')
print('Leer de una lista')
print('list_task[1]   : ', list_task[1] )
print('list_number[1] : ', list_number[1] )
print('\n')

print('====')
print('Agregar en la ultima posición de la lista')
print('====')
print('list_number ',  list_number.append(700))
print('\n')

print('====')
print('Agregar en una posicion específica')
print('====')
print('Agregar en una posicion de la lista')
print('list_number.insert(-1, 7)  ',  list_number.insert(-1,7))
print('list_number.insert(4, 6)  ',  list_number.insert(7,6))
print(list_number)
print('\n')


print('====')
print('Agregando')
print('====')
print('Agregar en una posicion de la lista')
print('list_number.insert(-1, 7)  ',  list_number.insert(-1,7))
print('list_number.insert(4, 6)  ',  list_number.insert(7,6))
print(list_number)
print('\n')


print('====')
print('Eliminando ')
print('====')
print('Agregar en una posicion de la lista')
print('list_number.pop()   ',  list_number.pop())
print('list_number.pop(0)  ',  list_number.pop(0))
print(list_number)
print('\n')

print('====')
print('Reverso de una lista ')
print('====')
print('list_number.reverse(): ')
list_number.reverse()
print(list_number)
print('\n')

print('====')
print('Sort')
print('====')
print('Ordenar una lista')
list_number.sort()
print(list_number)
