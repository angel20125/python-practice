import os
import random
os.system('clear')

print('=====')
print('clase 23: Indexing y slicing')
print('=====')
print('\n')
print('====')

##slicing
print('====')
print('indexing')
print('====')
text = "Ella sabe Python"
size = len(text)
print('text[0] = ',text[0])
print('text[1] = ',text[1])
print('Obteniendo la ultima posición')
print('size => ',size)
print(text[size - 1])
print(text[-1])
print ("\n")

# slicing
print('====')
print('slicing')
print('====')
print ("\n")
print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
