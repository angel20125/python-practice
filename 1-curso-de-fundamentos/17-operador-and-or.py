import os
os.system('clear')

print('=====')
print('clase 17: operadores AND y OR')
print('=====')
print('\n')

# AND
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)
print('\n')

print ('Ejemplo del operadore AND')
stock = input('Ingrese el numero de stock => ')
stock = int(stock)
print(stock >= 100 and stock <= 1000)
print('\n')

#OR
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)
print('\n')

print('Ejemplo del operador OR')
role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')
print('\n')
