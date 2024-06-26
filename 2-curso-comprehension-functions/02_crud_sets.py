import os
os.system('clear')

print('\n')
print('=====')
print('Clase 3 CRUD SETS (sets)')
print('=====')
print('\n')
'''
resumen
### Create

- `set( $param_1, $param_2...n )` : crear un conjunto y lo retorna

### read

- `size()`: muestra el tamaño del conjunto
- `in( $param )` : verifica si existe un elemento del conjunto

### update

- `add( $param )`:  Agregar un elemento al conjunto
- `update({ $param_1, $param_2})`: Actualiza el conjunto con un subconjunto `{}`

### delete

- `remove($param)`: Elimina un item `($param)` del conjunto, si no existe dará error  a
- `disacard($param)`: Elimina un item `($param)` del conjunto, si no existe no dará error  a como lo haría `remove($param)`
- `pop()`: el método pop se encarga de eliminar un elemento aleatorio del conjunto
- `clear()`: vacía el  conjunto
'''

set_contries = {}
set_contries = {'col', 'mex', 'bol'}

#Obtener el tamaño de un Conjunto
print('=====')
print('Tamaño de un conjunto')
print('=====')
size = len(set_contries)
print('size = len(set_contries)  :', size )
print('\n')
'''
#salida
=====
Tamaño de un conjunto
=====
size = len(set_contries)  : 3
'''


# - in
# Consultar si existe un valor
print('=====')
print('Consultar con el operador in')
print('=====')
print('¿Está "Col" en el conjunto?  :')
print('col' in set_contries)
print('¿Está "pe" en el conjunto?   :')
print('pe' in set_contries)
print('\n')
'''
#salida
=====
Consultar con el operador in
=====
¿Está "Col" en el conjunto?  :
True
¿Está "pe" en el conjunto?   :
False

'''

# - add
#Agregar un elemento a un conjunto
print('=====')
print('Agregar en el conjunto')
print('=====')
set_contries.add('pe')
print(set_contries)
print('\n')
'''
# salida
=====
Agregar en el conjunto
=====
{'mex', 'pe', 'bol', 'col'}
'''


# - update
#Actulizar el actual conjunto con un subconjunto {}
print('=====')
print('Actulizar un conjunto')
print('=====')
set_contries.update({'arg', 'ecua', 'ita'})
print(set_contries)
print('\n')
'''
#salida
=====
Actulizar un conjunto
=====
{'arg', 'pe', 'ecua', 'mex', 'ita', 'bol', 'col'}
'''

# - remove
# Remueve el item del conjunto, sino está el item el programa se detiene
print('=====')
print('Remover de un conjunto con "remove()" ')
print('=====')
print('Al utilizar remove debe existir el item a eliminar, sino dará error')
set_contries.remove('mex')
print(set_contries)
print('\n')
'''
=====
Remover de un conjunto con "remove()"
=====
Al utilizar remove debe existir el item a eliminar, sino dará error
{'arg', 'pe', 'ecua', 'ita', 'bol', 'col'}
'''

# - discard
# Remueve el items, si el item no esta el programa no se detiene
print('=====')
print('Remover de un conjunto con "discard" ')
print('=====')
print('Al utilizar discard NO dara error si el item no existe')
set_contries.discard('mex')
print(set_contries)
print('\n')
'''
#salida
=====
Remover de un conjunto con "discard"
=====
Al utilizar discard NO dara error si el item no existe
{'arg', 'pe', 'ecua', 'ita', 'bol', 'col'}
'''


# - pop
# Remueve  un elemento aleatorio
print('=====')
print('Remover de un conjunto con "pop" ')
print('=====')
print('Al utilizar pop remueve un elemento aleatorio')
set_contries.pop()
print(set_contries)
print('\n')
'''
#salida
=====
Remover de un conjunto con "pop"
=====
Al utilizar pop remueve un elemento aleatorio
{'pe', 'ecua', 'ita', 'bol', 'col'}
'''


# - clear
# vacia todo el conjunto
print('=====')
print('Remover de un conjunto con "clear" ')
print('=====')
print('Al utilizar clear vacia todo el conjunto')
set_contries.clear()
print(set_contries)
print('\n')
'''
#salida
=====
Remover de un conjunto con "clear"
=====
Al utilizar clear vacia todo el conjunto
set()
'''
