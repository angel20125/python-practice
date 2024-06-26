import csv
import os
import matplotlib.pyplot as plt

os.system('clear')
print('\n')
print('=====')
print('Clase 40 proyecto')
print('=====')


'''
  proyecto a partir de un archivo CSV que contiene los datos de la
  poblacion
'''


def read_csv(path):
  '''
    - funcion / return:
    Lee un archivo CSV y devuelve una lista de diccionarios con los
    datos del archivo

    -1 abre en modo lectura el archvio csv y renombrar como csvfile.
    -2 Se utiliza el método csv.reader(csvfile,delimiter=',')  para
    cargar el arhcivo.csv file  en una variable y le indicamos como
    están separados sus columnas con la coma','
    -3  el método next(reader) realizamos una iteración de forma
    manual obtiene. el objetivo es tener las cabecera/(titulos) de las
    columnas del archivo csvfile
    -4 Crea una lista vacia donde se almacenarán los datos del archivos
    -5 Se realiza un for() para recorrer 1 a 1 los registros del
    arhivo csv file.
    -6 Se utiliza el método zip(header,data) para generar una la estrutura iterable (header/data), header será la cabecera que se obtuvo anteriormente y data el registro de cada
    -7 Se crea el diccionario.
    -8 Se agrega el diccionario a la lista
    -9 retorna la lista de diccionarios
  '''
  with open(path, 'r') as csvfile: #1
    reader =csv.reader(csvfile, delimiter=',')#2
    header = next(reader)#3
    list_data=[]#4
    for data in reader:#5
      iterable=zip(header,data)#6
      country_dict = {key: value for key, value in iterable}#7
      list_data.append(country_dict)#8
  return list_data#9


def search_country_data(p_list, p_country):
  '''
    - funcion / return:
    Función para buscar en una lista un pais y luego retorna  en una
    lista el país con todos los datos el país buscado

    -1 Se utiliza el método filter(lambda item: item['Country/Territory'] == p_country, p_list) para filtrar la lista de paises con el país ingresado por el usuario
    -2 Se utiliza el método list(result) para convertir el resultado de la función filter en una lista.
    -3 retorna la lista
  '''
  result = filter(lambda item: item['Country/Territory'] == p_country, p_list)#1
  result = list(result)#2

  return result#3


def get_population(p_list_country):
  '''
    - funcion / return:
    función para retornar la poblacion de cada año
  '''
  population_dic = {
  '2022':int(p_list_country[0]['2022 Population']),
  '2020':int(p_list_country[0]['2020 Population']),
  '2015':int(p_list_country[0]['2015 Population']),
  '2010':int(p_list_country[0]['2010 Population']),
  '2000':int(p_list_country[0]['2000 Population']),
  '1990':int(p_list_country[0]['1990 Population']),
  '1980':int(p_list_country[0]['1980 Population']),
  '1970':int(p_list_country[0]['1970 Population'])

  }
  labels = population_dic.keys()
  values = population_dic.values()

  return labels, values

def generate_bar_chart(labels, values):
  '''
    - funcion / return:
    función para retornar la poblacion de cada año

    -1 fig, ax = plt.subplots(): Esta línea crea una nueva figura y un
    conjunto de ejes en esa figura. fig es la figura completa, mientras
    que ax es un solo conjunto de ejes en esa figura.

    -2 ax.bar(labels, values): Esta línea crea un gráfico de barras en
    el conjunto de ejes ax utilizando las etiquetas y valores
    proporcionados.

    -3 ax.pie(values, labels=labels): Esta línea crea un gráfico de
    torta en el conjunto de ejes ax utilizando los valores y etiquetas
    proporcionados

  '''
  fig, ax = plt.subplots() #1
  ax.bar(labels, values)#2
  plt.show()#3


if __name__:'__main__'
os.system('clear')
directory_file_csv = './Clases/40_data.csv'

print('=====')


country =input('Ingresa el país: ')
country =country.capitalize()
list_data = read_csv(directory_file_csv)
country_data = search_country_data(list_data,country)
labels, values = get_population(country_data)
generate_bar_chart(labels, values)

print(country_data)
print('\n')
print(  labels, values )
print('\n')

print('main')
