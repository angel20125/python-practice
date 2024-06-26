import os
os.system('clear')
print('\n')
print('=====')
print('Clase 23 Funcion filter')
print('=====')


'''
resumen
- función filter retorna una lista nueva donde están los items que cumplen la condición de filtrado
- la función filter no modifica la lista
'''

# - caso 1
print('\n')
print('- Caso 1, Mostrar los elementos pares de una lista')
print('-----')

list_numbers = [1,2,3,4,5,6,7,8,9,10]
list_numbers_pair = filter(lambda x: x % 2 == 0, list_numbers)
list_numbers_pair = list(list_numbers_pair)

print('Lista de numeros => ',list_numbers)
print('Lista de números pares => ',list_numbers_pair)
print('-----')
print('\n')

'''
- Caso 1, Mostrar los elementos pares de una lista
-----
Lista de numeros =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista de números pares =>  [2, 4, 6, 8, 10]
-----
'''


# - caso 2
print('\n')
print('- Caso 2, Mostrar los equipos que hayan ganado')
print('-----')
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new_list = filter(lambda list: list['home_team_result'] == 'Win', matches)
new_list =list(new_list)



print('\n')
print('-----')
print('Datos de los partidos ganados por los locales')
print(new_list)
print('\n')

print(' Partidos ganados por los locales: ')
print(len(new_list))
print('-----')
print('\n')

'''
salida

- Caso 2, Mostrar los equipos que hayan ganado
-----


-----
Datos de los partidos ganados por los locales
[{'home_team': 'Bolivia',
'away_team': 'Uruguay',
'home_team_score': 3,
'away_team_score': 1,
'home_team_result': 'Win'},

{'home_team': 'Ecuador',
'away_team': 'Venezuela',
'home_team_score': 5,
'away_team_score': 0,
'home_team_result': 'Win'}]


 Partidos ganados por los locales:
2
-----
'''
