import os
os.system('clear')

print('=====')
print('clase 19: if  elif')
print('=====')
print('\n')

print('Ejemplo 1')
print('=====')
print('En este primer ejemplo se evidencia como cambia el flujo del programa, Si el valor es True/False se muestra un mensaje diferente')
valor= True
if valor == True:
  print('debería ejecutarse')
if valor == False:
  print('nunca se ejecuta')

print('Ejemplo 2')
print('=====')
print('con elif le indicamos a python que no siga comparando si ya en algunos caso se cumplió la condición')
pet = input('Cuál es tu mascota favorita? ')
if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')
print('\n')

print('Ejemplo 3')
print('=====')
stock = int(input('Digita el stock => '))
if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')
print('\n')

#reto
number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')
