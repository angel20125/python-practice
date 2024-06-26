import os
import random
os.system('clear')

print('=====')
print('clase 33- ciclo for')
print('=====')
print('\n')


print('=====')
print('Ciclo for')
print('=====')
#se mostrará del 1 al 10
for element in range(1,11):
  print(element)
print('\n')

#salida
'''
=====
Ciclo for
=====
1
2
3
4
5
6
7
8
9
10
'''


print('=====')
print('Ciclo for con list')
print('=====')
my_list = [20,74,84,49]
print('my_list =', my_list)
for element in my_list:
  print(element)
print('\n')
#salida
'''
=====
Ciclo for con list
=====
my_list = [20, 74, 84, 49]
20
74
84
49
'''


print('=====')
print('Ciclo for con tuple')
print('=====')
my_tuple = ('nico', 'juli', 'santi')
print( 'my tuple = ', my_tuple  )
for element in my_tuple:
  print(element)
print('\n')
#salida
'''
=====
Ciclo for con tuple
=====
my tuple =  ('nico', 'juli', 'santi')
nico
juli
santi
'''


print('=====')
print('Ciclo for con diccionario ejemplo #1')
print('=====')
products = {
  'name': 'laptop',
  'price': 1000,
  'discount': 10,
  'category': 'computers'
}
print(products)
for key in products:
  print('atributo: ', key)
print('\n')
#salida
'''
Este caso se imprime las llaves básicamente

=====
Ciclo for con diccionario ejemplo #1
=====
{'name': 'laptop', 'price': 1000, 'discount': 10, 'category': 'computers'}
atributo:  name
atributo:  price
atributo:  discount
atributo:  category
'''


print('=====')
print('Ciclo for con diccionario ejemplo #2')
print('=====')
products = {
  'name': 'laptop',
  'price': 1000,
  'discount': 10,
  'category': 'computers'
}
print('products = ',products)
for key in products:
  print(key,'=>',products[key])
print('\n')

#salida
'''
Es este caso obtenmo el par value, key
=====
Ciclo for con diccionario ejemplo #2
=====
products =  {'name': 'laptop', 'price': 1000, 'discount': 10, 'category': 'computers'}
name => laptop
price => 1000
discount => 10
category => computers
'''



print('=====')
print('Ciclo for con diccionario ejemplo #3')
print('=====')
products = {
  'name': 'laptop',
  'price': 1000,
  'discount': 10,
  'category': 'computers'
}
print('products = ',products)
for key, value in products.items():
  print(key,'=>', value)
print('\n')
#salida
'''
=====
Ciclo for con diccionario ejemplo #3
=====
products =  {'name': 'laptop', 'price': 1000, 'discount': 10, 'category': 'computers'}
name => laptop
price => 1000
discount => 10
category => computers
'''



print('=====')
print('Ciclo for con lista/diccionario')
print('=====')
people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print(person)

print('\n')
for person in people:
  print('name =>  ', person['name'])

#salida
'''
=====
Ciclo for con lista/diccionario
=====
{'name': 'nico', 'age': 34}
{'name': 'zule', 'age': 45}
{'name': 'santi', 'age': 4}


name => nico
name => zule
name => santi
'''
