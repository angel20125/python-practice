import os
os.system('clear')

print('\n')
print('=====')
print('Clase 14 Scope de variables')
print('=====')
print('\n')

'''
#resumen
- Global scope: las variables global tienen alcance en un contexto
global

- Local scope: Las variables locales tienen alcance solamnente dentro
de un contexto local.

-Enclosing Scope:
Enclosing scope" o "alcance de cierre" en Python se refiere al nivel de
alcance en el que se encuentra una variable no global y no local
dentro de una función. Específicamente, se trata de una variable en la
función que contiene otra función. Cuando se define una variable en la
función externa y se utiliza en la función interna, la variable se
encuentra en el "Enclosing scope" para la función interna.
'''

print('Caso 1 : Global scope')
print('variables globales tienen un alcanze total')
print('=====')

# - caso 1
print('\n')
print('- Caso 1: llamada de una variable global en un contexto local')
print('--------')
msn_global= 'Hola, '
def saludo():
  msn_local='Mundo'
  print(msn_global + msn_local)
saludo()

'''
#salida

- Caso 1: llamada de una variable global en un contexto local
--------
Hola, Mundo
'''


# - caso 2
print('\n')
print('- Caso 2: a pesar de que una variable se llame igual existen dos contexto diferentes')
print('--------')

msn_global= 'Hola, '
def saludo ():
  msn_global ='Este mensaje es un contexto local'
  print(msn_global)
saludo()

'''
#salida
- Caso 2: a pesar de que una variable se llame igual existen dos contexto diferentes
--------
Este mensaje es un contexto local
'''


print('\n')
print('Caso 2 : Enclosing scope')
print('Si una funcion es declarada dentro de otra funcion, las variables que esten en la función padre serán accesible en la función hijo')
print('--------')

#caso - 2
def func_father():
  x = 300

  def func_son():
    print(x)

  func_son()

func_father()

'''
#salida

Si una funcion es declarada dentro de otra funcion, las variables que esten en la función padre serán accesible en la función hijo
--------
300

'''
