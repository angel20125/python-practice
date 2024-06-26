import os
os.system('clear')


print('\n')
print('=====')
print('Clase 18 "Higth order function" funciones')
print('=====')


'''
# resumen
Las funciones de orden superior en Python, también conocidas como
"High Order Functions", son aquellas funciones que pueden tomar una o
más funciones como argumentos, y/o retornar, al momento de ser llamadas
estás misma se encarga de realizar la llamada de la función que se
envía como argumento  junto a los parámatros y dar un resultado. Este
tipo de funciones son un concepto fundamental en la programación
funcional,
'''

# - caso 1
print('\n')
print('- Caso 1 Ejemplo de una "Higth order Function" ')
def sum(x):
  return x + 1
result_2 = sum(2)


def sum_hof(x, sum):
  return sum(x)
result_1 = sum_hof(2, sum)


print('Resultado  sum(2) /  sum_hof(2, sum)' )
print('_____')
print('Resultado de función normal                => ',result_1)
print('Resultado de función "higth order function"=> ',result_2)
'''
#salida
Resultado  sum(2) /  sum_hof(2, sum)'
_____

Resultado de función nomal                  => 3
Resultado de funcion "higth order function" => 3
'''



# - caso 2
print('\n')
print('- Caso 2 Ejemplo de una "Higth order Function" con "lambda function" ')

sum_hof_lambda = lambda x, func : func(x)
result_3 = sum_hof_lambda(2, sum)

print('Resultado sum_hof_lambda(2, sum)  ')
print('_____')
print('Resultado de función HOF con lamda => ',result_3)
'''
#salida
_____
Resultado de función HOF con lamda                 => 3

'''


# - caso 3
print('\n')
print('- Caso 3 Ejemplo de una "Higth order Function" con "lambda function')
print('Se puede enviar funciones lambda directamente en la llamada de las HOF')

sum_hof_lambda = lambda x, func : func(x)
result_3 = sum_hof_lambda(2, lambda x: x+1 )
print(' sum_hof_lambda(2, lambda x: x+1 ) =>',result_3)

result_3 = sum_hof_lambda(2, lambda x: x*5 )
print('sum_hof_lambda(2, lambda x: x*5 =>', result_3)

'''
 sum_hof_lambda(2, lambda x: x+1 ) => 3
 sum_hof_lambda(2, lambda x: x*5 => 10
'''
