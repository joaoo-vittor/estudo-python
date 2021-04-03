"""
Aula 13

Deque - Trabalhando com LIFO e FIFO

"""

from collections import deque

"""
fila = deque()

fila.append('joao')
fila.append('maria')
fila.append('jose')
fila.append('luiz')
fila.append('marcos')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for nome in fila:
    print(nome)
"""

fila = deque(maxlen=5)

fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)

print(fila)
