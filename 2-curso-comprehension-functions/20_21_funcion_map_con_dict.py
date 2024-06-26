import os
os.system('clear')
print('\n')
print('=====')
print('Clase 20 21 funcion map() "Higth order function"  con dict')
print('=====')

list_item = [
  {
    'product': 'camisa',
    'price': 100
  },
  {
    'product': 'pantalon',
    'price': 50
  },
  {
    'product': 'Sobrero',
    'price': 25
  },
]


# - caso 1
print('\n')
print('- Caso 1, Crear una lista de precios')
print('------')

list_price = map(lambda list: list['price'], list_item)
list_price = list(list_price)

print('- Invetario => :')
print(list_item)
print('\n')

print('- Lista de precios => :')
print(list_price)
print('\n')
'''
- Caso 1, Crear una lista de precios
------
- Invetario => :
[{'product': 'camisa', 'price': 100}, {'product': 'pantalon', 'price':
50}, {'product': 'Sobrero', 'price': 25}]


- Lista de precios => :
[100, 50, 25]
'''


# - caso 2
print('\n')
print('- Caso 2,Agregar un elemento de impuesto "taxes" al diccionario')
print('------')

def add_taxes (list):
  list_aux= list.copy() #!evitamos que la lista original sufra cambios
  list_aux['taxes'] = list_aux['price'] * 0.19
  return list_aux

list_update= map(add_taxes, list_item)
list_update= list(list_update)
print('- Invetario => :')
print(list_item)
print('\n')

print('- Lista de precios con "Taxes" => :')
print(list_update)
print('\n')

'''
#salida
- Caso 2, Agregar un elemento de impuesto "taxes" al diccionario
------
- Invetario => :
[{'product': 'camisa', 'price': 100}, {'product': 'pantalon', 'price':
50}, {'product': 'Sobrero', 'price': 25}]


- Lista de precios con "Taxes" => :
[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product':
'pantalon', 'price': 50, 'taxes': 9.5}, {'product': 'Sobrero', 'price':
25, 'taxes': 4.75}]

'''

# - caso 2
print('\n')
print('- Caso 2,Agregar un elemento de impuesto "taxes" al diccionario')
print('FORMA CORRECTA')
print('------')

def add_taxes (list):
  '''
  #* 1.crear una copia de la lista original, en otro espacio de memoria
  #* 2. Esto evita que la lista orignal sufra cambios.
  #* 3. Esto es, al trabajar con lista se trabaja con direccion de memoria
  '''
  list_aux= list.copy()
  list_aux['taxes'] = list_aux['price'] * 0.19
  return list_aux

list_update= map(add_taxes, list_item)
list_update= list(list_update)
print('- Invetario => :')
print(list_item)
print('\n')

print('- Lista de precios con "Taxes" => :')
print(list_update)
print('\n')
'''
- Caso ,Agregar un elemento de impuesto "taxes" al diccionario
FORMA CORRECTA
------
- Invetario => :
[{'product': 'camisa', 'price': 100}, {'product': 'pantalon', 'price':
50}, {'product': 'Sobrero', 'price': 25}]


- Lista de precios con "Taxes" => :
[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product':
'pantalon', 'price': 50, 'taxes': 9.5}, {'product': 'Sobrero', 'price':
25, 'taxes': 4.75}]
'''




# - caso 3
print('\n')
print('- Caso 3,Agregar un elemento de impuesto "taxes" al diccionario')
print('FORMA INCORRECTA')
print('Al no crear una copia se modifica la lista original')
print('------')

def add_taxes (list):
   #!al no crear una copia de la lista se modifica la lista original
  list['taxes'] = list['price'] * 0.19
  return list

list_update= map(add_taxes, list_item)
list_update= list(list_update)
print('- Invetario => :')
print(list_item)
print('\n')

print('- Lista de precios con "Taxes" => :')
print(list_update)
print('\n')
'''
- Caso 3,Agregar un elemento de impuesto "taxes" al diccionario
FORMA INCORRECTA
Al no crear una copia se modifica la lista original
------
- Invetario => :
[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product':
'pantalon', 'price': 50, 'taxes': 9.5}, {'product': 'Sobrero', 'price':
25, 'taxes': 4.75}]


- Lista de precios con "Taxes" => :
[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, {'product':
'pantalon', 'price': 50, 'taxes': 9.5}, {'product': 'Sobrero', 'price':
25, 'taxes': 4.75}]
'''
