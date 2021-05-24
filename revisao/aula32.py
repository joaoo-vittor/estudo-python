"""
Aula 32
"""

def converte_numero(valor):
  try:
    valor = int(valor)
    return valor
  except ValueError:
    try: 
      valor = float(valor)
      return valor
    except ValueError:
      return None


num = converte_numero(input('Digite um numero: '))

if num is not None:
  print(f'Soma de 5 + {num} = {num + 5}')
else:
  print('valor invalido')

