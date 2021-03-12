import random

geracpf = random.randint(100000000, 999999999)

cpf = str(geracpf)

aux = 10
acumulador = 0
for j in range(0, 2):
  for enu, i in enumerate(range(aux, 1, -1)):
    acumulador += int(cpf[enu]) * i

  digito = 11 - (acumulador % 11)

  if digito > 9:
    digito = 0
    cpf = cpf + str(digito)
  else:
    cpf = cpf + str(digito)

  aux += 1

print(f'O CPF gerado é {cpf}')
