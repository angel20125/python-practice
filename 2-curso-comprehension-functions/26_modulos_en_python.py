

import os
os.system('clear')

print('\n')
print('=====')
print('Clase 26 modulos en python')
print('=====')

'''
#resumen

Un módulo en Python es un archivo que contiene definiciones, funciones,
clases y variables que puedes usar una vez que se ha importado. Además,
un módulo puede incluir código ejecutable. Los módulos son una forma de
organizar las definiciones y las funciones relacionadas en un solo
archivo, lo que hace el código más legible y fácil de usar.
'''

#- caso 1
# Muestra el path donde se ejecuta el proyecto
import sys
print('import sys')
print('-------')
print('\n')
print(sys.path)


#- caso 2
# Modulo para trabajar con expresiones regulares
import re
print('\n')
print('import re')
print('-------')
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
# busqueda de numeros [0-9], el signo "+" significa que es más de 1

print(result)
'''
salida:
import re
-------
['311', '123', '121', '57', '3'
'''


#- caso 3
# Modulo para trabajar con el tiempo
print('\n')
import time
print('import time')
print('-------')
timestamp = time.time()
print(timestamp)

local = time.localtime() #obtiene la hora
result = time.asctime(local) #da un formato a la hora
print(result)

'''
salida:
import time
-------
1718323362.7557843
Thu Jun 13 20:02:42 2024
'''


#- caso 4
# Modulos para trabajar con lista
print('\n')
import collections
print('import collection')
print('-------')

print('Cuenta la cantidad de incidencia de un número')
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)

'''
salida:

import collection
-------
Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})
'''
