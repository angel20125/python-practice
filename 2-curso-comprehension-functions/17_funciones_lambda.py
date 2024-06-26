import os
os.system('clear')


print('\n')
print('=====')
print('Clase 17 lamda funciones')
print('=====')

'''
#resumen
En Python, una función lambda es una pequeña función anónima. Una
función lambda puede tomar cualquier número de argumentos, pero solo
puede tener una expresión. Se definen utilizando la palabra clave
`lambda`.

La sintaxis de una función lambda es: `lambda arguments: expression`

La expresión se evalúa y se devuelve. Las funciones lambda pueden ser
usadas donde sea necesario un objeto de función.
Por ejemplo, una función lambda que suma dos argumentos podría verse
así:

suma = lambda a, b: a+b
print(suma(5, 3))  # Salida: 8

En el código de arriba, `suma` es una función lambda que toma dos
argumentos, `a` y `b`, y devuelve su suma. Cuando llamamos a `suma(5, 3)
`, la función devuelve `8`

'''



# - caso 1
print('\n')
print('- Caso 1 función para incrementa un valor sin lambda function')
print('------')
def sum (x):
  return x+1
print(sum(1))


# - caso 2
print('\n')
print('- Caso 2 función para incrementa un valor con lambda function')
print('------')
sum_l = lambda x : x + 1
print( sum_l(1) )

'''
#salida
- Caso 1 función para incrementa un valor sin lambda function
------
2


- Caso 2 función para incrementa un valor con lambda function
------
2
'''
