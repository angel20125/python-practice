print("=====")
print("clase 9: string")
print("=====")
print("\n")


print("concatenacion de string")
print("=====")
name = "Nicolas"
last_name = 'Molina Monroy'
full_name = name + " " + last_name
print(full_name)
print("\n")

print("Incluir grámatica dentro de la cadenas de texto")
print("=====")
quote = "I'm Nicolas"
quote2 = ' She said "Hello"  '
print(quote)
print(quote2)
print("\n")


# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)
print("\n")

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)
print("\n")

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)
print("\n")
