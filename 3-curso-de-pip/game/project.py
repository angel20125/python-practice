import os
os.system('clear')

print('\n')
print('=====')
print('Clase 13 funciones retornar más de un valor')
print('=====')
print('\n')





import os
import random
os.system('clear')

print('=====')
print('clase 37: proyecto final')
print('=====')
print('\n')

options = ('piedra', 'papel', 'tijera')
rounds=0
computer_wins =0
user_wins =0

while True:

  rounds += 1
  print('\n')
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  print('=== Puntuacion ===')
  print('Computadora: ', computer_wins)
  print('Jugador: ', user_wins)
  print('\n')
  print('*' * 10)
  # fin del juego si el usuario o computadora llega a los 3 puntos
  if computer_wins == 3 or user_wins == 3:
    print('!!!! fin del juego')
    print('Puntuación final')
    print('computadora 🤖:  ',computer_wins)
    print('usuario 🦸: ', user_wins)
    break
  #selección de opciones
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)
  # si la opción no es valida saltara el bloque de condicionales
  if not user_option in options:
    print('esa opcion no es valida')
    continue
  '''
  1. El primer if es para saber si están empatados
  2. Los siguientes elif evalua todos los casos donde gana el jugador,
  en caso contrario gana la computadora.
  '''
  if user_option == computer_option:
    print('=====')
    print('empate')
    print('=====')
    print('Computadora🤖: ', computer_option)
    print('Jugador🦸: ', user_option)
    print('\n')
  elif user_option == 'piedra' and computer_option == 'tijera':
    print('=====')
    print('Jugador Gana!')
    print('=====')
    print('Computadora🤖: ', computer_option)
    print('Jugador🦸: ', user_option)
    user_wins +=1
    print('\n')
  elif user_option == 'tijera' and computer_option == 'papel':
    print('=====')
    print('Jugador Gana!!')
    print('=====')
    print('Computadora🤖: ', computer_option)
    print('Jugador🦸: ', user_option)
    user_wins +=1
    print('\n')
  elif user_option == 'papel' and computer_option == 'piedra':
    print('=====')
    print('Jugador Gana!!!')
    print('=====')
    print('Computadora🤖: ', computer_option)
    print('Jugador🦸: ', user_option)
    user_wins +=1
    print('\n')
  else:
    print('=====')
    print('Computadora Gana!!!')
    print('=====')
    print('Computadora🤖: ', computer_option)
    print('Jugador🦸: ', user_option)
    computer_wins+=1
