import csv
import os
os.system('clear')

print('\n')
print('=====')
print('Clase 37 leer un csv')
print('=====')

'''
https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
resumen

'''



def read_csv(path):
  '''
  función:
    Lee un archivo csv y retorna una lista de diccionario
  parametros:
    path: ruta del archivo csv
  retunr:
    Una lista  de diccionario

  nota: cada fila del csv representa un fila de datos, la primera fila
  del csv  representa la cabecera de los datos y las siguientes fila
  son data, una vez se tenga la cabecera la idea es tener  un lista con
  (header:data)

  1- En modo lectura abre/lee el  archivo csv y lo renombra como
  csvfile. la sentencia with abre el archivo y una vez se halla
  terminado su uso lo cierra.
  2- asignamos el archivo csv a una variable, para recorrer el archivo
  en indicamos el limitador.
  utilizamos el método csv.reader(csvfile,delimiter=',')

    En Python, <class '_csv.reader'> es una clase que representa un
    objeto lector de CSV. Se utiliza para leer datos de un archivo CSV
    fila por fila. Cada fila se devuelve como una lista de valores
    separados por comas.

  3- La primera fila del archivo es la cabecera de los datos se guardan
  en una variable
  4- Se declara una lista vacia para guarda un lista de diccionario con
  {header:data}
  5- Con un for recorremos el csv cargado en la variable reader
  6- Mientras recorremos el archivo creamos una variable iterable con
  la función zip(header,data) para crear una tupla y luego trasnfomarla
  en un diccionario {header,data}
  luego transformalos en un diccionario {header,data}
  7- transformamos  el itreable  que es un tupla (header:data) a un
  diccionario country {header:data}, nos apoyamos en dictonary
  comprhension
  8- agregamos de forma individual cada diccionario a la lista definida en el paso 4
  9- finalmente retornamos la data

  '''

  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') #2
    header = next(reader)#3
    list_data=[]#4

    for data in reader: #5
      iterable=zip(header,data)#6
      country_dict = {key: value for key, value in iterable}#7
      list_data.append(country_dict)#8
    return list_data#9


if __name__ == '__main__':
  file='./Clases/37_data.csv'
  list_country = read_csv(file)
  print(list_country[0])

'''
=====
Clase 37 leer un csv
=====
{
  'Rank': '36',
  'CCA3': 'AFG',
  'Country/Territory': 'Afghanistan',
  'Capital': 'Kabul',
  'Continent': 'Asia',
  '2022 Population':'41128771',
  '2020 Population': '38972230',
  '2015 Population': '33753499',
  '2010 Population': '28189672',
  '2000 Population': '19542982',
  '1990 Population': '10694796',
  '1980 Population': '12486631',
  '1970 Population': '10752971',
  'Area (km²)': '652230',
  'Density (per km²)': '63.0587',
  'Growth Rate': '1.0257',
  'World Population Percentage': '0.52'
}
'''
