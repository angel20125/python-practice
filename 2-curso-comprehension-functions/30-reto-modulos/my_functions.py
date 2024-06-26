def get_totals(orders):
  '''
    - order: es unas lista de diccionarios
    - Funcion: en encargada crear una lista que solo tenga el total de
    - retunr: una lista
    cada orden de compra
    se utiliza list comphension
  '''
  result= [order['total'] for order in orders]
  print('resultado get_totals() =>',result, type(result))
  return result

def calc_total(totals):
  result =sum(totals)
  print('resultado cal_total() =>', result)
  return result
