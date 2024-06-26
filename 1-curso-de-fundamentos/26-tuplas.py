import os
import random
os.system('clear')

print('=====')
print('clase 26: tuplas')
print('=====')
print('\n')


number = (1,2,3,4)
string = ('nico','nico','zule','santi')

print('======')
print('Dato y tipo de dato')
print('======')
print("\n")
print('Tutpla  number  : ', number)
print('tipo de dato    : ', type(number))
print('=====')
print('tipo de dato    : ', type(string))
print('Tutpla  string  : ', string)
print('=====')


print('=====')
print('Ubicar un elemento en la tupla')
print('=====')
print('Indice ubicación de "zule" : ', string.index('santi'))
print('Indice ubicación de "nico" : ', string.count('nico'))

print('=====')
print('las tuplas no permiten modificaciones')
print('=====')
print('1- convertimos tuplas en lista')
my_list=list(string)
print('2- convertimos realizamos los cambios')
my_list[1]= 'Juli'
print('3- convertimos la lista en tupla')
my_tuple=tuple(my_list)
print('lista  : ', my_list)
print('tupla  : ', my_tuple)
