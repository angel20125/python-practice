import utils
import os
os.system('clear')

print('\n')
print('=====')
print('Clase 28  Ejemplo:2 modulos en python como script')
print('=====')
'''
resumen

- Para configurar un archivo que se ejecute como un script debemo seguir
dos pasos:


 1- colocar todo la lógica dentro de una función . run()
ejemplo:
  def run():
    logica principal

 2- colocar la llamada de ese función principal . run() dentro de un if __name__ == '__main__' ejemplo:

if __name__ == '__main__':
  run()


'''

# - Caso 0
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




def run():

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


if __name__ == '__main__':
  run()
