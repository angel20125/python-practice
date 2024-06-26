import os
import random
os.system('clear')

print('=====')
print('clase 31- reto de diccionario')
print('=====')
print('\n')

'''
En este desafío, se te proporcionará un diccionario llamado `person` que contiene información sobre una persona. Tu reto es realizar las siguientes operaciones en orden:

1. Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
2. Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
3. Eliminar el elemento del diccionario con la llave "age".
4. Imprimir una lista con las llaves del diccionario.
5. Imprimir una lista con los valores del diccionario.
'''

person = {
  'name': 'Nicolas',
  'lastName': 'Molina',
  'age': 29
}

#solución 👇 #1
print('====')
print('Solucion #1')
print('====')
person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
print(  list(person.keys())   )
print(  list(person.values())  )
print('\n')


person = {
  'name': 'Nicolas',
  'lastName': 'Molina',
  'age': 29
}


#solución 👇 #2
print('====')
print('Solucion #2')
print('====')
person.update({"twitter":"@nicobytes"})
person['name'] = "Felipe"
person.pop('age')
print(  list(person.keys())    )
print(  list(person.values())  )
print('\n')
