print('\n')
print('=====')
print('Clase 32 Errores en Python')
print('=====')

'''
resumen
La declaración assert en Python se utiliza para realizar una
verificación de depuración. Se asegura de que una condición específica
sea verdadera. Si la condición es verdadera, el programa continúa
ejecutándose; si es falsa, el programa lanza un error AssertionError.
Por ejemplo, assert 2 + 2 == 4 no hará nada porque la condición es
verdadera, pero assert 2 + 2 == 5 lanzará un AssertionError.

raise Exception en Python se utiliza para lanzar una excepción
intencionalmente. Puedes especificar un mensaje de error para indicar
qué salió mal. Por ejemplo, raise Exception('Algo está mal')
interrumpirá el flujo normal del programa y mostrará el mensaje ‘Algo
está mal’ como parte del error. Es útil para manejar errores y casos
especiales en tu código.
'''

# - caso 1
print('\n')
print('- Caso 1: assert')
print('--------')
print('\n')

suma = lambda x,y: x + y
assert suma(2,2) == 4 , 'Este mensaje se mostrará si no cumple'
print('assert ok, => Continua la ejecución del programa')

'''
- Caso 1: assert
--------


assert ok, => Continua la ejecución del programa
'''


# - caso 2
print('\n')
print('- Caso 2: raise Exeption')
print('--------')
print('\n')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 2')
'''

- Caso 2: raise Exeption
--------

detiene la ejecución del programa

raise Exception('No se permiten menores de edad')
Exception: No se permiten menores de eda
'''
