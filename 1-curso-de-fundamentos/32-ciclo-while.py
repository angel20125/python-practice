import os
import random
os.system('clear')

print('=====')
print('clase 32- ciclo while')
print('=====')
print('\n')


print('=====')
print( 'Utilizando el ciclo while' )
print('=====')
counter=0
while counter < 10:
  counter +=1
  print( counter )
print ('\n')

#la sentencia break rompe el ciclo
print('=====')
print( 'While / break' )
print('=====')
print(' En este ejemplo se imprimira del 1 al 14')
counter=0
while counter < 20:
  counter +=1
  if counter == 15:
    break
  print( counter )
print ('\n')


#la senticia continue salta a la siguiente iteracion, ignora toda la logica
print('=====')
print( 'While / continue' )
print('=====')
print(' En este ejemplo se mostrará del 15 al 20')
counter=0
while counter < 20:
  counter +=1
  if counter < 15:
    continue
  print( counter )
print ('\n')
