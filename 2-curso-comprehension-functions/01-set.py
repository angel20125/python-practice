import os
os.system('clear')

print('\n')
print('=====')
print('Clase 2 Cojunto (sets)')
print('=====')
print('\n')
'''
resumen
- Para crear un conjunto se utilizan las llaves `{}` o la función `set()
- Se pueden añadir elementos a un conjunto utilizando el método `add()`.
- Para eliminar un elemento usamos el método `remove()`.
- Los conjuntos también soportan operaciones matemáticas como la unión, intersección, diferencia y diferencia simétrica.
- Se pueden modificar
- No tienen un orden
- No pueden tener elementos duplicados
'''


#se puede establecer un conjunto a partir de un string
print('====')
print('Conjunto string')
print('====')
set_contries = {'col', 'mex', 'bol'}
print('set_contries            :', set_contries       )
print('type(set_contries)      :', type(set_contries) )
print('\n')
set_from_string = set('hooolaaa')
print('set_from_string        : ',  set_from_string       )
print('type(set_from_string)  : ',  type(set_from_string) )
print('\n')
'''
#salida
====
Conjunto string
====
set_contries            : {'bol', 'mex', 'col'}
type(set_contries)      : <class 'set'>


set_from_string        :  {'l', 'o', 'h', 'a'}
type(set_from_string)  :  <class 'set'>
'''



#Conjunto a partir de números
print('====')
print('Conjunto Numeros')
print('====')
set_numbers = {1,2,2,443,23}
print('show set numbers    : ', set_numbers   )
print('type(set_numbers)   : ',  type(set_numbers) )
print('\n')
'''
1. Al momento de mostrar los conjuntos no se muestran los valores repetido

#salida
====
Conjunto Numeros
====
show set numbers    :  {1, 2, 443, 23}
type(set_numbers)   :  <class 'set'>
'''



#Conjunto a partir distintos tipos de datos
print('====')
print('Conjunto de distintos tipos de datos')
print('====')
set_types = {1, 'hola', False, 12.12}
print(' set_types: ', set_types )
print('\n')
'''
1. El orden en el que se muestran los conjuntos no importa
#salida
====
Conjunto de distintos tipos de datos
====
 set_types:  {False, 1, 'hola', 12.12}

'''

#conjunto a partir de una estructura de datos "tuplas"
print('====')
print('Conjunto de un tupla')
print('====')
my_tuple = ( 'abc', 'cbv', 'as', 'abc')
set_from_tuples = set(my_tuple)
print(' set_from_tuples  : ', set_from_tuples )
print('\n')
'''
#salida
====
Conjunto de un tupla
====
 set_from_tuples  :  {'as', 'cbv', 'abc'}
'''

#conjunto a partir de una estructura de datos "Lista"
print('====')
print('Conjunto de un lista')
print('====')
my_list = [1,2,3,1,2,3,4]
set_from_list = set(my_list)
print(' set_from_list  : ', set_from_list )
print('\n')

print('Transformando los conjuntos en lista')
list_unique_numbers = list(set_from_list)
print('list_unique_numbers  :', list_unique_numbers)
print('\n')

'''
#salida
====
Conjunto de un lista
====
 set_from_list  :  {1, 2, 3, 4}


Transformando los conjuntos en lista
list_unique_numbers  : [1, 2, 3, 4]
'''
