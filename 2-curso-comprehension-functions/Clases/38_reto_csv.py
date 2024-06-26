import csv
import os
os.system('clear')

print('\n')
print('=====')
print('Clase 38 reto leer un csv')
print('=====')

'''
Console
Pruebas
Para resolver este desafío, debes utilizar el archivo data.csv que
contiene los datos de los gastos de una empresa. El archivo tiene dos
columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y
calcula el total de gastos de la empresa. Para leer el archivo CSV,
puedes utilizar la función open y el módulo csv de Python. Una vez que
hayas leído los datos, puedes calcular el total de gastos implementando
la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60
'''



'''
1- con el  sentencia with abrir/leer el archivo csv renombrarlo como
"csvfile"
2- cargar el archivo en una variable reader usando el método
csv.reader(csvfile,delimiter=',')
3- recorrer la variable reader con un for
4- Se suma cada elemento que hay en cada lista en la posición 1
'''
import csv

def read_csv(path):
   # Tu código aquí 👇
   total = 0
   with open(path,'r') as csvfile: #1
      reader = csv.reader(csvfile,delimiter=',')#2
      for row in reader:#3
         total += int(row[1])
   return total

response = read_csv('./Clases/38_data.csv')
print('total :', response)

'''

=====
Clase 38 reto leer un csv
=====
total : 1499

'''
