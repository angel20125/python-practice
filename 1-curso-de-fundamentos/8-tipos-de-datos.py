print("=====")
print("clase 8: tipos de datos")
print("=====")
print("\n")



#type es una funcion que nos indica el tipo de datos

#tipo de datos: string
print("Tipo de datos string")
print("=====")
my_name= "Angel"
my_last_name= 'Quintero'
print("Name: ", my_name)
print("last Name:", my_last_name)
print("tipo de dato de my_age: ", type(my_name))
print("tipo de dato de my_las_name: ", type(my_last_name))
print("\n")
'''
#salida

Tipo de datos string
=====
Name:  Angel
last Name: Quintero
tipo de dato de my_age:  <class 'str'>
tipo de dato de my_las_name:  <class 'str'>
'''



#Tipo de datos: int

print("Tipo de datos int")
print("=====")
my_age=27
print("Age",my_age)
print("tipo de dato de my_age: ", type(my_name))
print("\n")
'''
#salida

Tipo de datos int
=====
Age 27
tipo de dato de my_age:  <class 'str'>
'''


#Tipo de datos: boolean True / False, la primera letra de True/false debe ser mayuscula
print("Tipo de datos boolean")
print("=====")
is_single= True
print("is single",is_single)
print("tipo de dato de my_age: ", type(is_single))
print("\n")
'''
#salida

Tipo de datos boolean
=====
is single True
tipo de dato de my_age:  <class 'bool'>
'''

#Los tipos de datos ingresados por consolas son string
print("Ingrese sus edad y su nombre")
print("=====")
my_name = input("Ingrese su nombre:  ")
my_age = input("Ingrese su edad:  ")
print("Su nombre es: ",my_name," y su edad es: ",my_age," años")
print("Tipo de dato my_age, my_name ", type(my_age) ," ", type(my_name))
print("Tipo de dato de la variable my_age, my_name")

print("\n")
'''
#salida

Ingrese sus edad y su nombre
=====
Ingrese su nombre:  Angel
Ingrese su edad:  Quintero
Su nombre es:  Angel  y su edad es:  Quintero  años
Tipo de dato my_age, my_name  <class 'str'>   <class 'str'>
Tipo de dato de la variable my_age, my_name
'''
