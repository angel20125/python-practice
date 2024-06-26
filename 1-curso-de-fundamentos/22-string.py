import os
import random
os.system('clear')

print('=====')
print('clase 22: String Recargo')
print('=====')
print('\n')

text = 'Ella sabe programar en Python'
text_2 = 'este es un titulo'

print('======')
print(' "in" ')
print('======')
print(' TEXT = ', text)
print('\n')
print('Se encuentra "JavaScript" en el string text:' )
print('JavaScript' in text)
print('Se encuentra "Python" en el string text: ')
print('Python' in text)
print('\n')

'''
#salida
'''

print('Lenguaje de programacion que escojiste')
if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')
print('\n')

print('======')
print(' "len()" ')
print('======')
print(' TEXT = ', text)
size = len(text)
print('total de caracteres: ', size)
print('\n')


print('======')
print(' ".upper() .lower() .count()" ')
print('======')
print(' TEXT = ', text)
print('text.upper()     = ',  text.upper())
print('text.lower()     = ',  text.lower())
print('text.count("a")  =',   text.count('a'))
print('\n')


print('======')
print(' ".swapcase() .startwith() .endwith()" ')
print('======')
print(' TEXT = ', text)
print('text.swapcase()              =', text.swapcase())
print('text.startswith("Ella")      =', text.startswith('Ella'))
print('text.endswith("Rust")        =', text.endswith('Rust'))
print('text.replace("Python', 'Go") =', text.replace('Python', 'Go'))
print('\n')


print('======')
print(' ".capitalize() .title() .isdigit()" ')
print('======')
print(' TEXT_2 = ', text_2)

print('text_2.capitalize()   =',text_2.capitalize())
print('text_2.title()        =',text_2.title())
print('text_2.isdigit()      =',text_2.isdigit())
print(' esto es un número  "398" ',"398".isdigit())


'''

python3 22-string.py
=====
clase 22: String Recargo
=====


======
 "in"
======
 TEXT =  Ella sabe programar en Python


Se encuentra "JavaScript" en el string text:
False
Se encuentra "Python" en el string text:
True


Lenguaje de programacion que escojiste
Tambien elegiste bien


======
 "len()"
======
 TEXT =  Ella sabe programar en Python
total de caracteres:  29


======
 ".upper() .lower() .count()"
======
 TEXT =  Ella sabe programar en Python
text.upper()     =  ELLA SABE PROGRAMAR EN PYTHON
text.lower()     =  ella sabe programar en python
text.count("a")  = 4


======
 ".swapcase() .startwith() .endwith()"
======
 TEXT =  Ella sabe programar en Python
text.swapcase()              = eLLA SABE PROGRAMAR EN pYTHON
text.startswith("Ella")      = True
text.endswith("Rust")        = False
text.replace("Python Go") = Ella sabe programar en Go


======
 ".capitalize() .title() .isdigit()"
======
 TEXT_2 =  este es un titulo
text_2.capitalize()   = Este es un titulo
text_2.title()        = Este Es Un Titulo
text_2.isdigit()      = False
 esto es un número  "398"  True
'''
