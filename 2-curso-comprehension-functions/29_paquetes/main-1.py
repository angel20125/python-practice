

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


# Caso 1
print('- Caso 1, importar paquete utilizando la sentencia')
print(' from <nombre_paquete> import <nombre_func_1>')
print('___________')
print('\n')

'''
- Al usar la senctencia: "from <nombre_paquete> import <nombre_func_1>"
para importar paquetes, lo unico que hay que tener en cuent es que puede haber dos funciones con el mismo nombre y puede empezar ha chocar
-En ambos caso si existe un archivo "__init__.py" el archivo se llama si o si.
'''

from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4


print('Ejecuión de => ',func_1())
print('Ejecuión de => ',func_2())
print('Ejecuión de => ',func_3())
print('Ejecuión de => ',func_4())
