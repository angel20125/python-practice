import os
os.system('clear')

print('\n')
print('=====')
print('Clase 4 Operaciones de conjunto')
print('=====')
print('\n')


'''
### resumen

- union
La union de conjunto consiste en unir dos conjuntos sin repetir los elementos
- intersection
La intercepción consiste en  mostrar los elementos en común
- difference
Consiste en crear un nuevo conjunto con los elementos del  conjunto 1, que no sean comunes entre el conjunto 1 y conjunto 2. Aparte que no tengo los elementos del conjunto 2
- Symmetric Difference
Consiste en crear un nuevo conjunto con los elementos no comunes de conjunto 1 y conjunto 2
'''


# - union
#La union de conjunto consiste en unir dos conjuntos sin repetir los elementos
print('=====')
print('Union de conjuntos')
print('=====')
set_contries = {'col', 'mex', 'bol'}
set_contries_2 = {'bol', 'pe'}
set_union = set_contries.union(set_contries_2)
print('conjunto 1 : ', set_contries)
print('conjunto 2 : ', set_contries_2)
print('union      : ',set_union)
print('Tambien se puede unir los conjuntos con operador "|" ')
print(set_contries | set_contries_2)
print('\n')
'''
# salida
=====
Union de conjuntos
=====
conjunto 1 :  {'mex', 'col', 'bol'}
conjunto 2 :  {'bol', 'pe'}
union      :  {'mex', 'bol', 'col', 'pe'}
Tambien se puede unir los conbjuntos con operador "|"
{'mex', 'bol', 'col', 'pe'}
'''


# - intersection
#La intercepción consiste en  mostrar los elementos en común
print('=====')
print('Intercepcion de conjuntos')
print('=====')
set_contries = {'col', 'mex', 'bol'}
set_contries_2 = {'bol', 'pe'}
set_intercepcion = set_contries.intersection(set_contries_2)
print('conjunto 1   : ', set_contries)
print('conjunto 2   : ', set_contries_2)
print('intercepción : ', set_intercepcion )
print('Tambien se puede interceptar los conjuntos con operador "&" ')
print(set_contries & set_contries_2)
print('\n')
'''
#salida

=====
Intercepcion de conjuntos
=====
conjunto 1   :  {'col', 'bol', 'mex'}
conjunto 2   :  {'pe', 'bol'}
intercepción :  {'bol'}
Tambien se puede interceptar los conjuntos con operador "&"
{'bol'}
'''

# - difference
# Consiste en crear un nuevo conjunto con los elementos del  conjunto 1 que no sean comunes entre el conjunto 1 y conjunto 2. Aparte que no tengo los elementos del conjunto 2
print('=====')
print('Diferencia de conjuntos')
print('=====')
set_contries = {'col', 'mex', 'bol'}
set_contries_2 = {'bol', 'pe'}
set_difference = set_contries.difference(set_contries_2)
print('conjunto 1 : ', set_contries)
print('conjunto 2 : ', set_contries_2)
print('difference      : ',set_difference)
print('Se puede hacer diferencia de conjuntos con el operador "-" ')
print(set_contries - set_contries_2)
print('\n')
'''
#salida
=====
Diferencia de conjuntos
=====
conjunto 1 :  {'bol', 'mex', 'col'}
conjunto 2 :  {'bol', 'pe'}
difference      :  {'mex', 'col'}
Se puede hacer diferencia de conjuntos con el operador "-"
{'mex', 'col'}
'''


# - Symmetric Difference
# Consiste en crear un nuevo conjunto con los elemento no comunes de conjunto 1 y conjunto 2
print('=====')
print('Diferencia simétrica de conjuntos')
print('=====')
set_contries = {'col', 'mex', 'bol'}
set_contries_2 = {'bol', 'pe'}
set_symmetric_difference = set_contries.symmetric_difference(set_contries_2)
print('conjunto 1 : ', set_contries)
print('conjunto 2 : ', set_contries_2)
print('set_symmetric_difference      : ',set_symmetric_difference)
print('Se puede hacer diferencia simetrica de conjuntos con el operador "^" ')
print(set_contries ^ set_contries_2)
'''
#salida
=====
Diferencia simétrica de conjuntos
=====
conjunto 1 :  {'bol', 'mex', 'col'}
conjunto 2 :  {'bol', 'pe'}
set_symmetric_difference      :  {'pe', 'mex', 'col'}
Se puede hacer diferencia simetrica de conjuntos con el operador "^"
{'pe', 'mex', 'col'}
'''
