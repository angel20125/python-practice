import os
os.system('clear')

print('=====')
print('clase 16: comparación de float')
print('=====')
print('\n')

x = 3.3
y = 1.1 + 2.2
print('el valor x :',x, 'tipo de dato: ', type(x))
print('el valor y :',x, 'tipo de dato: ', type(y))
print('Son iguales x == y :', x == y)
print('\n')

print('1° Primera forma para comprar:' )
print('Es llevando ambos modelos a string')
print('====')
y_str = format(y, ".2g")
x_str = str(x)
print('x_str :',x_str, 'tipo de dato: ', type(x_str))
print('y_str :',x_str, 'tipo de dato: ', type(y_str))
print('son iguales :',y_str == x_str)
print('\n')

print('2° Segunda forma de comprar:' )
print('la segunda forma  es creando un nivel de tolerancia')
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)
print('\n')


print('3° Tercera forma de comprar:' )
print('La tercera forma es utilizando la funcion round')
x=3.36
y=3.30
y = round(y,1)
x = round(x,1)
print('x :',x)
print('y :',y)
print('x == y ', (x == y) )


print('3° Tercera forma de comprar QUE NO DA IGUAL:' )
print('La tercera forma es utilizando la funcion round')
x=3.36
y=3.30
y = round(y,1)
x = round(x,1)
print('x :',x)
print('y :',y)
print('x == y ', (x == y) )
