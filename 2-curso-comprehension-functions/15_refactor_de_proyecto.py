import random
import os
os.system('clear')

print('\n')
print('=====')
print('Clase 14 refactor de proyecto')
print('=====')
print('\n')

options = ('piedra', 'papel', 'tijera')
rounds=0
computer_wins =0
user_wins =0

# - funtion
def isfinal_games(p_user_wins, p_computer_wins):
  '''
    Funcion para saber si el juego termino
    p_computer_wins: numero de veces que gana la computadora
    p_user_wins: numero de veces que gana el jugador
    return: True, fin del juego / return False juego aun no ha terminado
  '''
  if p_computer_wins == 3 or p_user_wins == 3:
    return True
  return False


def choose_option_user():
  '''
  Funcion para elegir la opcion del jugador
  return None, si la opción no es valida
  rerurn user_option, si la opcion esta válida
  '''
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  if not user_option in options:
    print('esa opcion no es valida')
    return None
  return user_option


def choose_option_computer():
  '''
  Funcion para elegir la opcion de la computadora
  return computer_option, una opción aleatoria
  '''
  computer_option = random.choice(options)
  return computer_option

def playing_game( p_user_option, p_computer_option ):
  '''
    Funcion para saber quien gana el juego
    1. El primer if es para saber si están empatados
    2. Los siguientes elif evalua todos los casos donde gana el jugador,
    en caso contrario gana la computadora.
  '''
  if p_user_option == p_computer_option:
    print('=====')
    print('empate')
    print('=====')
    print('Computadora🤖: ', p_computer_option)
    print('Jugador🦸: ', p_user_option)
    print('\n')
  elif p_user_option == 'piedra' and p_computer_option == 'tijera':
    print('=====')
    print('Jugador Gana!')
    print('=====')
    print('Computadora🤖: ', p_computer_option)
    print('Jugador🦸: ', p_user_option)
    user_wins +=1
    print('\n')
  elif p_user_option == 'tijera' and p_computer_option == 'papel':
    print('=====')
    print('Jugador Gana!!')
    print('=====')
    print('Computadora🤖: ', p_computer_option)
    print('Jugador🦸: ', p_user_option)
    user_wins +=1
    print('\n')
  elif p_user_option == 'papel' and p_computer_option == 'piedra':
    print('=====')
    print('Jugador Gana!!!')
    print('=====')
    print('Computadora🤖: ', p_computer_option)
    print('Jugador🦸: ', p_user_option)
    user_wins +=1
    print('\n')
  else:
    print('=====')
    print('Computadora Gana!!!')
    print('=====')
    print('Computadora🤖: ', p_computer_option)
    print('Jugador🦸: ', p_user_option)
    computer_wins+=1
  return


#main logic
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
  if isfinal_games(computer_wins,user_wins):
    print('!!!! fin del juego')
    print('Puntuación final')
    print('computadora 🤖:  ',computer_wins)
    print('usuario 🦸: ', user_wins)
    break
  #selección de opciones
  user_option = choose_option_user()
  computer_option =choose_option_computer()

  # si la opción no es valida saltara el bloque de condicionales
  if not user_option in options:
    print('esa opcion no es valida')
    continue
  playing_game(user_option,computer_option)
