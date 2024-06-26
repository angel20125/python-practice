import os
os.system('clear')


print('\n')
print('=====')
print('Clase 19 funcion map() "Higth order function" ')
print('=====')

'''
#resumen
- La función map() en Python es una función de orden superior (HOF) que
toma una función y un iterable como argumentos, y devuelve un nuevo
iterable con la función aplicada a cada argumento.

-Si la función map () trabaja sobre dos lista y una  lista es de
menor tamaño que la otra lista,  entonces la función map() toma como
referencia el tamaño de la lista de menor amplitud para realizar las
iteaciones

- la funcicon map() retorna una referencia de la memoria, es por ello
que al momento de recibir el resulta se debe hacer lo siguiente
result = list(result)

'''


list_numbers_1 = [1,2,3,4]
list_numbers_aux = []

# - caso 1
print('\n')
print('- Caso 1, Utilizando una función map()')
print('------')

def square (n):
  return n*2

#sin function map()
for numbers in list_numbers_1:
  list_numbers_aux.append(square(numbers))

# con function map()
result = map(square, list_numbers_1)
result = list(result)
print(' Resultado sin function map => ',list_numbers_aux)
print(' Resultado con function map => ',result)
'''
salida:

- Caso 1, Utilizando una función map()
------
 Resultado sin function map =>  [2, 4, 6, 8]
 Resultado con function map =>  [2, 4, 6, 8]
'''


# - caso 2
print('\n')
print('- Caso 2, Función map con lambda ')
print('------')
list_numbers_aux.clear()


for number in list_numbers_1:
  list_numbers_aux.append(number*2)

# result = list (  map (lambda i: i*2,list_numbers_1)  )
result = map (lambda i: i*2,list_numbers_1)
result = list(result)
print(' Resultado sin function map => ',list_numbers_aux)
print(' Resultado con function map => ',result)
'''
- Caso 2, Función map con lambda
------
 Resultado sin function map =>  [2, 4, 6, 8]
 Resultado con function map =>  [2, 4, 6, 8]
'''

# - caso 3
print('\n')
print('- Caso 3, Función map con lista de distantas dimensiones lambda ')
print('------')

numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7,8,7]

result = map( lambda x,y: x+y, numbers_1, numbers_2  )
result = list(result)
print(' Resultado con function map => ',result)
