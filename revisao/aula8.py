"""
Aula 8

Desempacotando lista

"""

lista1 = [1, 2, 3]
lista2 = [i for i in range(1, 11)]

v1, v2, v3 = lista1
n1, n2, *resto = lista2

print(v1, v2, v3)
print(n1, n2, resto)

