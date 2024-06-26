import os
import random
os.system('clear')

print('\n')
print('=====')
print('Clase 8 dict comprenhension con condicionales')
print('=====')
print('\n')

print('=====')
print('Ejemplo 1 de dict comprhension con condicionales')
print('=====')
print('\n')
print('Ejemplo -2 Generar un diccionario "population", "clave:valor"  a partir de dos lista donde el país sera la clave y la población será el valor, el número de la población se genera a partir de un una función aleatoria')
print('\n')
print('a- Luego de generado el diccionario crear un nuevo diccionario con los paises que tienen una población menor a 50 personas ')
print('\n')

countries = ['col', 'mex', 'bol', 'pe']
population = {}

# - parte 1 sin dict comprehension
print('Sin dict comprehension')
for country in countries:
  population[country] = random.randint(1,100)
print(population)

# - parte 1 con dict comprehension
print('Con dict comprehension')
population.clear()
population = {country : random.randint(1,100) for country in countries }
print(population)

print('Filtrando valores')
result = { country : population for (country, population) in population.items() if population < 50}
print(result)

'''
#salida

Sin dict comprehension
{'col': 36, 'mex': 100, 'bol': 46, 'pe': 21}
Con dict comprehension
{'col': 71, 'mex': 87, 'bol': 76, 'pe': 28}
Filtrando valores
{'pe': 28}
'''

print('\n')
print('=====')
print('Ejemplo 2 de dict comprhension con condicionales')
print('=====')
print('\n')
print('Generar un diccionario clave:valor que solo tenga vocales extraida de un texto. key( clave) sera la vocal en minúscula  y el value (valor) sera el la vocal en mayúsculas')

text = 'Hola, soy Angel'
unique = { char :char.upper() for char in text  if char in 'aeiou'}
print(unique)

'''
#salida
{'o': 'O', 'a': 'A', 'e': 'E'}

'''



print('\n')
print('=====')
print('Ejemplo 3 de dict comprhension con condicionales')
print('=====')
print('\n')
print('Generar un diccionario key:value (clave:valor) que solo tenga vocales extraida de un texto el valor (key) sera la vocal en minúscula y el valor (value) el número de veces que se encuentra la vocal en la frase')

text = 'Hola, soy Angel'

unique = {char:text.count(char) for char in text  if char in 'aeiou' }
print(unique)

'''
#salida
{'o': 2, 'a': 1, 'e': 1}

'''
