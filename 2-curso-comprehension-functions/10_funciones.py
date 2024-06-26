import os
import random
os.system('clear')

print('\n')
print('=====')
print('Clase 10 funciones en python')
print('=====')
print('\n')

'''
#resumen
Las funciones en Python son bloques de código reutilizables que realizan una tarea específica. Se definen usando la palabra clave `def`, seguida por el nombre de la función y paréntesis `()`. Los argumentos de la función van dentro de los paréntesis. El cuerpo de la función se indentado y comienza después de los dos puntos `:`. Puede devolver un valor usando la palabra clave `return`.

Aquí hay un ejemplo de una función en Python:
'''

def saludo(nombre):
  return "Hola, " + nombre

print(saludo("Mundo"))  # Salida: Hola, Mundo
print('\n')



def suma(a, b):
  return(a + b)

print( suma(1 ,5)  )# 6
print( suma(10, 4) ) # 14
print('\n')


'''
#salida

Hola, Mundo

6
14
'''
