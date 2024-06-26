
import os
os.system('clear')
print('\n')
print('=====')
print('Clase 36 Escribir en un archivo')
print('=====')

'''
resumen
- open(<'/directorio-del-archivo'>) : abre un archivo
- open(<'/directorio-del-archivo'>, <forma de apertura>) :
  abre un archivo con una forma de apertura
  - 'r' : solo lectura
  - 'w' : solo escritura
  - 'a' : solo escritura al final
  - 'r+' : lectura y escritura pero no  borra el contenido del archivo
  - 'w+' : lectura y escritura pero borra el contenido del archivo
  - 'a+' : lectura y escritura pero no borra el contenido del archivo
- close() : cierra un archivo
- file.seek(0): pocision la lectura del archivo desde el principio

'''

with open('./texs.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')
