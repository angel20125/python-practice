import os
import random
os.system('clear')

print('=====')
print('clase 28: Diccionario')
print('=====')
print('\n')

print('Declaracion  "my_dict={}" ')
my_dict = {}
print('tipo de datos')
print(type(my_dict))
print('\n')

my_dict = {
  'nombre': 'Juan',
  'apellido': 'Perez',
  'edad': 25,
}

print('=====')
print('mostrando el diccionario y su tamñaño')
print('=====')
print('Datos diccionario')
print(my_dict)
print('\n')
print('tamaño del diccionario')
print(len(my_dict))
print('\n')


#obtener datos con get para evitar el programa se detenga
print('=====')
print('obteniendo datos del diccionario')
print('=====')
print(my_dict['nombre'])
print(my_dict.get('apellido'))
print('\n')


#se puede validar con el operador in si existe la clave
print('=====')
print('obteniendo datos del diccionario')
print('=====')
print('Existe la clave "nombre" ')
print('nombre' in my_dict)
print('\n')

print('Existe la clave "empleo" ')
print('empleo' in my_dict)
print('\n')
