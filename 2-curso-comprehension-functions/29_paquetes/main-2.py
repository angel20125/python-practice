import os

import pkg.mod_2
os.system('clear')


print('\n')
print('=====')
print('Clase 29 paquetes en python')
print('=====')

'''
Se puede importar paquetes de dos formas:

1- Utilizando la sentencia
from <nombre_paquete> import <nombre_func_1, nombre_func_2...n>
esta forma es compatible con la version 3.3  de python

2- Utilizando un archivo "__init__.py" este método era utilizado antes
de la version 3.3 en python

3- El archivo __init__.py en Python se utiliza para marcar un
directorio como un paquete de Python. Esto permite que puedas importar
módulos desde ese directorio. Si tienes un directorio con varios
archivos .py y quieres poder importar esos módulos, debes incluir un
archivo __init__.py en el directorio. Puede estar vacío, pero su
presencia indica a Python que trate el contenido del directorio como un
paquete.
'''

# Caso 2
print('- Caso 2, importar paquete utilizando el archivo:')
print(' __init__py')
print('___________')
print('\n')

import pkg
'''
- Este import, le indicará a python que busque el archivo "__init__py",
ya que este archivo le indica a python que trate esa carpeta como un
paquete
- Este método es recomendado ya que estarimaos utilizando
namespace.
- La llamada de las funciones son más explicitas mencionando a cual pequete pertence la función a utilizar
'''


print('Ejecuión de =>', pkg.URL)
print('Ejecuión de => ',pkg.mod_1.func_1())
print('Ejecuión de => ',pkg.mod_1.func_2())
print('Ejecuión de => ',pkg.mod_2.func_3())
print('Ejecuión de => ',pkg.mod_2.func_4())

'''
- Caso 2, importar paquete utilizando el archivo:
 __init__py
___________


platzi.com
Ejecuión de =>  Func 1
Ejecuión de =>  Func 2
Ejecuión de =>  Func 3
Ejecuión de =>  Func 4
'''
