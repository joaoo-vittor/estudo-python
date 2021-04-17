import random

geracpf = random.randint(100000000, 999999999)

def verificaCpf(cpf):

  cpf = formataCpf(cpf)
  aux = cpf
  digito_verificador = cpf[-2:]

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

  return cpf

def formataCpf(cpf):
  tamanho = len(cpf)
  novo_cpf = cpf[:11].split('.')
  digito = cpf[-2:]
  novo_cpf = ''.join(novo_cpf)
  if tamanho > 9:
    return novo_cpf + digito
  return novo_cpf

check_cpf = verificaCpf('168.995.350-09')
# check_cpf = verificaCpf(str(geracpf))

if check_cpf:
  print('Valido.')
else:
  print('invalido.')
