
'''
  modulo que tiene  funciones para mostrar  país/población
'''

list_country = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def get_population():
  '''
    Función para mostrar lo población  con su pais
  '''
  keys = ['Colombia', 'Bolivia']
  values = [500, 300]
  return keys, values



def population_by_country(p_list, p_country):
  '''
    Función para buscar en una lista un pais y luego retorna  en una
    lista el país junto a su población
  '''
  result = filter(lambda item: item['Country'] == p_country, p_list)
  result = list(result)
  return result
