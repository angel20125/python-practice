import os
import random
os.system('clear')

print('=====')
print('clase 24: Lista')
print('=====')
print('\n')
print('====')

types = [1, True, 'hola']
numbers = [1, 2, 3, 4]
tasks = ['make a dishes', 'play videogames']

print(numbers)
print(tasks)
print(types)
print('\n')

print('tipo de dato de lista numbers :',type(numbers))
print('tipo de dato de lista task :',type(tasks))
print('tipo de dato de lista  types:',type(types))
print('\n')

print('Accediendo a un valor de la lista')
print('numbers[0] = ',numbers[0])
print('tasks[0] = ', tasks[0])
print('\n')

print('Reemplazo de un valor en la lista')
print(' tasks[0] = "watch platzi courses"  ')
print(' tasks[1] = "do the dishes" ')
tasks[0] = 'watch platzi courses'
tasks[1] = 'do the dishes'
print(tasks)
print('\n')

print ('Usando el operador in')
print('True in types = ', True in types)
print(' "hola" in types = ','hola' in types)
print('\n')

print('Recoriendo una lista')
print(' numbers[:3] =',numbers[:3])
print(' numbers[:-1] =',numbers[:-1])
