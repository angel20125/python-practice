
import os
os.system('clear')

print('\n')
print('=====')
print('Clase: 31 iterables')
print('=====')


'''
- Iteradores de Python
Un iterador es un objeto que contiene un número contable de valores.
Un iterador es un objeto sobre el que se puede iterar, lo que significa
que puede recorrer todos los valores.
Técnicamente, en Python, un iterador es un objeto que implementa el
protocolo del iterador, que consta de los métodos __iter__() y __next__
().

- Iterador vs Iterable
Las listas, tuplas, diccionarios y conjuntos son todos objetos
iterables. Son contenedores iterables de los que puede obtener un
iterador.
Todos estos objetos tienen un iter()método que se utiliza para obtener
un iterador:


- Se asigna el elemento que se quiere recorrer o iterar a la función
iter()

- luego se usa la función next() para recorrer o iterar el objeto.

- Cuando se termina de recorrer el objeto, la función next() lanza una
excepción de tipo StopIteration.
'''

# - caso 1
print('\n')
print('Caso 1, Recorriendo un string')
print('-------')
print('\n')

# - caso 1
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''

Caso 1, Recorriendo un string
-------

b
a
n
a
n
a

'''


# - caso 2
print('\n')
print('Caso 2, Recorriendo un rango')
print('-------')
print('\n')

my_iter = iter(range(1, 4))
print('Muestra una direccion => ',my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
'''
#print(next(my_iter))
si ejecutaramos una vez más  la función nex(), se generaría una
excepción de tipo StopIteration. porque range solo genera números
del 1 al 3
'''


'''
Muestra una direccion =>  <range_iterator object at 0x7b8f35457f30>
1
2
3
'''
