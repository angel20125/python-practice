print('=====')
print('clase 13: Transformación de tipos')
print('=====')
print('\n')


print('int')
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int('3') # z will be 3
print('x = int(1)   ', type(x))
print('y = int(2.8) ', type(y))
print('z = int("3") ', type(z))
print('\n')

print('Floats:')
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float('3')   # z will be 3.0
w = float('4.2') # w will be 4.2
print('x = float(1)    ', type(x))
print('y = float(2.8)  ', type(y))
print('z = float("3")  ', type(z))
print('w = float("3")  ', type(z))
print('\n')

print('String')
x = str('s1') # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print('x = float("s1")    ', type(x))
print('y = float(2)       ', type(y))
print('z = float("3.0")   ', type(z))
print('\n')


print('Todo los datos suministrado por input son de tipo str')
age = input('Escribe tu edad => ')
print('tipo de dato de eadad ANTES del cast: ',type(age))
age = int(age)
print('tipo de dato de eadad DESPUES del cast: ',type(age))
age += 10
print(f'Tu edad en 10 años será {age}')
