import os
os.system('clear')

print('\n')
print('=====')
print('Clase 6 list comprenhension')
print('=====')
print('\n')


'''
### resumen
La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista basada en los valores de una lista existente.

'''

#- list comprenhension
list_number_1 = []
list_number_2 = []

print('=====')
print('Ejemplo 1 de list comprhension')
print('=====')
print('\n')
print('Ejemplo -1 Generar una lista de números del 1 al 10 y cada elemento multiplicarlo por 2')

# - parte 1 sin list comprehension
for element in range(1,11):
  list_number_1.append(element * 2)
print(list_number_1)

# - parte 2 con list comprehension
list_number_2 = [element * 2 for element in range(1,11)]
print(list_number_2)

'''
# salida
Ejemplo -1 Generar una lista de números del 1 al 10 y cada elemento multiplicarlo por 2
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''


print('\n')
print('=====')
print('Ejemplo 2 de list comprhension con condiciones')
print('=====')
print('\n')
print('Ejemplo -2 Generar una lista de números pares del 1 al 10 y cada elemento multiplicarlo por 2')

# - parte 1 sin list comprehension
list_number_1.clear()
for element in range(1,11):
  if element%2 ==0:
    list_number_1.append(element * 2)
print(list_number_1)


# - parte 2 con list comprehension
list_number_2.clear()
list_number_2 = [element*2 for element in range(1,11) if element%2 ==0]
print(list_number_2)

'''
# salida
Ejemplo -2 Generar una lista de números pares del 1 al 10 y cada elemento multiplicarlo por 2
[4, 8, 12, 16, 20]
[4, 8, 12, 16, 20]
'''


print('\n')
print('=====')
print('Ejemplo 3 de list comprhension con condiciones')
print('=====')
print('\n')
print('Ejemplo -2 a partir de un lista de fruta genera una nueva lista de frutas que contenga  la letra "a" ')


# - parte 1 sin list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# - parte 2 sin list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

'''
Ejemplo -2 a partir de un lista de fruta genera una nueva lista de frutas que contenga  la letra "a"
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
'''
