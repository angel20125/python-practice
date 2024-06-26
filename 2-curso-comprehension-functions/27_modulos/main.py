import utils
import os
os.system('clear')



print('\n')
print('=====')
print('Clase 27 modulos en python')
print('=====')

'''
resumen
- los nombre de los modulos no pueden comenzar con numeros

- todos los archivos de python se puede decir que se tratan como
módulos.

- Se puede ejeutar las funciones utilizando el nombre del modulo con
la siguiente sintaxis "modulos.funcion()" o modulo.variable

- Un módulo en Python es una colección de funciones y declaraciones de
Python en un solo archivo. Los módulos se utilizan para organizar y
reutilizar el código. Puedes crear tus propios módulos o utilizar
módulos incorporados en Python o proporcionados por terceros. Para
utilizar un módulo en tu programa, primero debes importarlo utilizando
la declaración import.

'''
print('\n')
print('- Caso 0,  utilizando  "modulo utils" importar   ')
print(' la variable list_country')
print('-----')
print('Mostrando los datos importado')
data=[]
data=utils.list_country.copy()
print(data)
'''
- Caso 0,  utilizando  "modulo utils" importar
 la variable list_country
-----
Mostrando los datos importado
[{'Country': 'Colombia', 'Population': 500}, {'Country': 'Bolivia', 'Population': 300}]
'''


# - caso 1
print('\n')
print('- Caso 1,  utilizando el "modulo utils" ejecutar la función ')
print(' "get_population" y mostra los paises y su población ')
print('-----')

keys, values = utils.get_population()
print(keys, values)
'''

- Caso 1,  utilizando el "modulo utils" ejecutar la función
 "get_population" y mostra los paises y su población
-----
['Colombia', 'Bolivia'] [500, 300]
'''

# - caso 2
print('\n')
print('- Caso 2,  utilizando le "modulo utils" ejecutar la función')
print(' "utils.population_by_country(p_list,p_country)"  ')
print(' esto para ubicar  un país en la lista y mostrar su población')
print('-----')
country = input('Type Country => ').capitalize()
result = utils.population_by_country(data,country)
print(result)
'''
- Caso 2,  utilizando le "modulo utils" ejecutar la función
 "utils.population_by_country(p_list,p_country)"
 esto para ubicar  un país en la lista y mostrar su población
-----
Type Country => colombia
[{'Country': 'Colombia', 'Population': 500}]
'''
