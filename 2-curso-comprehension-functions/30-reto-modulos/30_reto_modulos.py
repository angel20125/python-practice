
import os
os.system('clear')

print('\n')
print('=====')
print('Clase 30 reto modulos en python')
print('=====')

'''
En este desafío, se te presenta una lista de objetos que representan órdenes de compra con los siguientes atributos:

customer_name: string
total: number
delivered: boolean
Tu reto es utilizar el concepto de módulos de Python para retornar la suma total de todas las órdenes de compra. Para resolver el ejercicio, debes trabajar en el archivo main.py, donde se encuentra la función get_total. Esta función recibe como parámetro la lista de órdenes de compra.

Debes retornar la suma total de todas las órdenes haciendo uso de las funciones definidas en el archivo my_functions.py.my_functions.py.

Ejemplo:

Input:
[
  {
    customerName: "Nicolas",
    total: 100,
    delivered: true,
  },
  {
    customerName: "Zulema",
    total: 120,
    delivered: false,
  },
  {
    customerName: "Santiago",
    total: 20,
    delivered: false,
  }
]

Ouput:
240
'''
import my_functions as mf

def get_total(orders):
  # Tu código aquí 👇
  total=mf.calc_total(mf.get_totals(orders))
  return total

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)

'''

=====
Clase 30 reto modulos en python
=====
resultado get_totals() => [100, 120, 20] <class 'list'>
resultado cal_total() => 240
240

'''
