"""
Aula 9

Torcando valor de variaveis

"""

x = 10
y = 69

print(f'y={y} x={x}\n')

aux = x
x = y
y = aux

print(f'y={y} x={x}')

x, y = y, x

print(f'y={y} x={x}')

print('\n###########################\n')

"""
Operações Ternarias
"""

log = True

msg = 'Usuario Logado' if (log == True) else 'Usuario precisa logar'

print(msg)
