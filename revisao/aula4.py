"""

Formatando Valores com modificadores

:s -> String
:d -> Inteiro
:f -> Numero de ponto flutuante
:.(NUMERO)f - Quantidade de casas decimais -> :.2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> -> Esquerda
< -> Direita
^ -> Centro

"""

nome = 'João'

print(f'{nome:*^50}')
