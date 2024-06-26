import os
os.system('clear')

print('=====')
print('clase 18: operadores NOT')
print('=====')
print('\n')


print('not')
print(not True)
print(not False)
print('\n')

print('Ejemplo del operadore NOT')
stock = input('Ingrese el numero de stock => ')
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))
