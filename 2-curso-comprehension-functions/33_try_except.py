import os
os.system('clear')
print('\n')
print('=====')
print('Clase 33 try except')
print('=====')


# - Caso 1
print('Caso 1, try-except por separados')
print('--------')
print('\n')

try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)
print(' I caso 1, Continua la ejecución del programa')
print('\n')


try:
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print(error)
print(' II caso 1, Continua la ejecución del programa')
print('\n')


try:
  assert 1 != 1, '1  si es igual a 1'
except AssertionError as error:
  print(error)
print(' III caso 1, Continua la ejecución del programa')
print('\n')

'''
salida
division by zero
 I, Continua la ejecución del programa


No se permiten menores de edad
 II, Continua la ejecución del programa


1  si es igual a 1
 III, Continua la ejecución del programa
'''





# - Caso 2
'''
En este caso el muestra la primera excepción
'''
print('Caso 2 , try-except juntos')
print('--------')
print('\n')

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('IV Caso 2, Ejecución del código')
'''
Caso 2 , try-except juntos
--------


division by zero
IV Caso 2, Ejecución del código
'''
