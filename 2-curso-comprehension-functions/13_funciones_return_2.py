import os
import random
os.system('clear')

print('\n')
print('=====')
print('Clase 13 funciones retornar más de un valor')
print('=====')
print('\n')

print('- Ejemplo 1: Una función con los valores por parámatros defecto en los parámetros, al momento de la llamada tenemos dos opciones para llamar a la función')
print('1) llamar la función sin argunmentos')
print('2) llamar la función solo con un argumento')

print('-------')
print('\n')
def find_volumen(length=10, width=10, depth=10):
  return length * width * depth

# - caso 1
print('llamada sin argumento "find_volumen()" ')
result = find_volumen()
print(result)

# -  caso 2
print('llamada con 1 argumento  "find_volumen(width=1)" ')
result = find_volumen(width=1)
print(result)


'''
#salida

llamada sin argumento "find_volumen()"
1000
llamad con 1 argumento "find_volumen(width=1)"
100
'''

print('\n')
print('- Ejemplo 2: Se puede retornar más de un valor con el return, en este caso, lo que se debe hacer es; separar los valores con comas. Existe dos formas de guardar los valores')
print('\n')

print('1- Guardar  los valores en dos variables separadas')
print('2- Guardar los valores en una sola variable y se vera como una tupla')
def find_volumen_2(length=10, width=10, depth=10):
  respond= length * width * depth
  return 'Este es el resultado es: ', respond

# - caso 1
msn,result  = find_volumen_2()
print(msn, result)
print('\n')

# - caso 2
result = find_volumen_2()
print('result      =>  ' ,result)
print('result[1]   =>  ' ,result[1])
'''
#salida


result      =>   ('Este es el resultado es: ', 1000)
result[1]   =>   1000

'''
