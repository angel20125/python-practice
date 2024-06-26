import os
os.system('clear')
print('\n')
print('=====')
print('Clase 39 Crear Gráficos')
print('=====')


'''
El código Python proporcionado define una función llamada
generate_bar_chartque crea un gráfico de barras. Aquí hay un desglose
del código:

Importar:

import matplotlib.pyplot as plt: Esta línea importa el pyplot módulo de
la matplotlib biblioteca y le asigna el alias plt. se usa comúnmente
para crear visualizaciones en Python. pyplot

Definición de función:
def generate_bar_chart(labels, values):: Esto define una función
denominada generate_bar_chartque toma dos argumentos: y . Se espera que
estos argumentos sean listas que contengan datos para el gráfico.
labelsvalues

Creando el gráfico:
fig, ax = plt.subplots(): Esta línea crea una nueva figura ( fig) y un
ax objeto de ejes ( ) usando la función plt.subplots() . La figura
representa el gráfico general y los ejes definen el área donde se
trazarán las barras.

Trazando las barras:
ax.bar(labels, values): esta línea es donde se crea el gráfico de
barras real. Utiliza el barmétodo del axobjeto. Este método toma dos

argumentos:
labels: Esta es la lista que proporcionó que contiene etiquetas para
cada barra en el eje X.

values: Esta es la lista que contiene los valores correspondientes a
cada barra. La altura de cada barra vendrá determinada por estos
valores.

Mostrando el gráfico:
plt.show(): Esta línea muestra el gráfico generado en la pantalla.

En resumen, este código define una función que simplifica la creación
de un gráfico de barras. Puede llamar a esta función con sus datos
(etiquetas y valores) para generar y mostrar el gráfico.
'''



'''
Detalles del código:

import matplotlib.pyplot as plt: Esta línea importa el módulo pyplot de
la biblioteca matplotlib y lo renombra como plt para facilitar su uso
en el código.

fig, ax = plt.subplots(): Esta línea crea una nueva figura y un
conjunto de ejes en esa figura. fig es la figura completa, mientras que
ax es un solo conjunto de ejes en esa figura.

ax.bar(labels, values): Esta línea crea un gráfico de barras en el
conjunto de ejes ax utilizando las etiquetas y valores proporcionados.

ax.pie(values, labels=labels): Esta línea crea un gráfico de torta en
el conjunto de ejes ax utilizando los valores y etiquetas
proporcionados.

ax.axis('equal'): Esta línea asegura que el gráfico de torta se dibuje
como un círculo en lugar de una elipse, estableciendo la relación de
aspecto de los ejes a ‘equal’.

plt.show(): Esta línea muestra la figura. Esto abrirá una ventana con
el gráfico de torta.
'''
import matplotlib.pyplot as plt
print('\n')
print('=====')
print('Clase 39 reto leer un csv')
print('=====')

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #descomentar para
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
