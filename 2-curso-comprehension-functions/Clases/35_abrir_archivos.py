
import os
os.system('clear')
print('\n')
print('=====')
print('Clase 35 Lectura de un archivo')
print('=====')

'''
resumen
- open(<'/directorio-del-archivo'>) : abre un archivo
- close() : cierra un archivo
- read() : lee el contenido del archivo
- readline() : lee una linea del archivo
- with : lee el archivo y una vez haya leido el archivo lo cierra
 with open(<'/directorio-del-archivo'> as file:
  for line in file:
    print(line)

'''
file = open('./35_text.txt')


print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file:
  print(line)

file.close()

with open('./35_text.txt') as file:
  for line in file:
    print(line)
