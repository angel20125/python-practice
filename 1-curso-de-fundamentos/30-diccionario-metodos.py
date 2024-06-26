import os
import random
os.system('clear')

print('=====')
print('clase 30: Diccionarios: inserción y actualización')
print('=====')
print('\n')


person = {
  'name': 'Juan',
  'last_name': 'Perez',
  'age': 25,
  'job': 'programador',
  'langs': ['python', 'javasacritp']
}

print('====')
print('mostrando diccionario')
print('====')
print(person)
print('\n')

print('====')
print('Actulizando datos de person')
print('====')
print('  person["name"] = "santi"          ')
print('  person["age"]+=10                 ')
print('  person["langs"].append("rust")    ')
person['name']= 'santi'
person['age']+=10
person['langs'].append('rust')

print('\n')
print(person)
print('\n')

print('====')
print('Borrando datos un objeto')
print('====')
print(' del person ["last_name"] ')
print(' person.pop("age")        ')
del person ['last_name']
person.pop('age')

print('\n')
print(person)
print('\n')


print('====')
print('mostrando items')
print('====')

print(  'person.items()'   )
print(   person.items()    )
print('\n')

print('====')
print('mostrando keys')
print('====')

print(  'person.keys()'   )
print(   person.keys()    )
print('\n')


print('====')
print('mostrando values')
print('====')

print(  'person.values()'   )
print(   person.values()    )
print('\n')
