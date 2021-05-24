"""

CPF = 168.995.350-09
------------------------------------------------

 1° Passo                   2° Passo
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
        297           #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9

"""

cpf = '168.995.350-09'

# cpf = str(input('Digite seu CPF: '))

digito_verificador = cpf[-2:]
novo_cpf = cpf[:11].split('.')
novo_cpf = ''.join(novo_cpf)

aux_cpf = ''
aux = 10
acumulador = 0
for j in range(0, 2):
  for enu, i in enumerate(range(aux, 1, -1)):
    acumulador += int(novo_cpf[enu]) * i

  digito = 11 - (acumulador % 11)

  if digito > 9:
    digito = 0
    novo_cpf = novo_cpf + str(digito)
  else:
    novo_cpf = novo_cpf + str(digito)

  aux += 1

if novo_cpf[-2:] == digito_verificador:
  print(f'CPF {cpf} é valido.')
else:
  print(f'CPF {cpf} é invalido.')



