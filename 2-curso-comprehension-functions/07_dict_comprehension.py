import os
import random
os.system('clear')

print('\n')
print('=====')
print('Clase 7 dict comprenhension')
print('=====')
print('\n')


'''
### resumen

Dictionary comprehension  ofrece una sintaxis más corta cuando desea crear un nuevo diccionario basado en los valores de una lista existente.

'''

print('=====')
print('Ejemplo 1 de dict comprhension')
print('=====')
print('\n')
print('Ejemplo -1 Generar un diccionario (clave:valor) donde la clave  seria del 1 al 5 y donde el valor seria  también numero del 1 al 5 mutiplicado por 2')
print('\n')

# - parte 1 sin dict comprehension
dict_1 = {}
for i in range (1,6):
  dict_1[i] = i*2
print(dict_1)


# - parte 2 con dict comprehension
dict_2 = {}
dict_2 = { i : i*2 for i in range(1,6) }
print(dict_2)

'''
#salida
Ejemplo -1 Generar un diccionario (clave:valor) donde la clave  seria del 1 al 5 y donde el valor seria  también numero del 1 al 5 mutiplicado por 2


{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
'''

print('=====')
print('Ejemplo 2 de dict comprhension')
print('=====')
print('\n')
print('Ejemplo -2 Generar un diccionario "population", "clave:valor"  a partir de dos lista donde el país sera la clave y la población será el valor, el número de la población se genera a partir de un una función aleatoria')
print('\n')

countries = ['col', 'mex', 'bol', 'pe']
population = {}

# - parte 1 sin dict comprehension
for country in countries:
  population[country] = random.randint(1,100)
print(population)

# - parte 1 con dict comprehension
population.clear()
population = {country : random.randint(1,100) for country in countries }
print(population)
'''
#salida

Ejemplo -2 Generar un diccionario "population", "clave:valor"  a partir de dos lista donde el país sera la clave y la población será el valor, el número de la población se genera a partir de un una función aleatoria


{'col': 2, 'mex': 48, 'bol': 64, 'pe': 87}
{'col': 53, 'mex': 57, 'bol': 56, 'pe': 5}
'''

print('=====')
print('Ejemplo 3 de dict comprhension' )
print('=====')
print('\n')
print('Ejemplo -3 Generar un diccionario a partir de dos lista, donde el elemento clave(key), debe ser  el nombre y elemento valor (value) debe ser el elemento  edad')
print('\n')

# parte 1 sin dict comprenhension
names = ['nico', 'zule', 'santi']
ages = [20, 25, 30]
print(   dict(zip(names,ages))  )


# parte 2 con dict comprehension
new_dict = { name:age for (name, age) in zip(names,ages) }
print(new_dict)


# parte 3 con dict comprenhension
# Crédito: Adolfo Sebastián Jara Gavilanes (at platzi)
new_dict.clear()
new_dict = new_dict = {names[i]:ages[i] for i in range(len(names))}
print(new_dict)
print('\n')

'''
Ejemplo -3 Generar un diccionario a partir de dos lista, donde el elemento clave(key), debe ser  el nombre y elemento valor (value) debe ser el elemento  edad


{'nico': 20, 'zule': 25, 'santi': 30}
{'nico': 20, 'zule': 25, 'santi': 30}
{'nico': 20, 'zule': 25, 'santi': 30}
'''
