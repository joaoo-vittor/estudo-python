"""
Aula 6

Lista

append, insert, pop, del, clear, extend
min, max
range

"""

l1 = [1, 2, 3, 4, 5]
l2 = [i for i in range(1, 10)]

print(l1)

# Insere a string "joao" na posição 0 da lista
l1.insert(0, 'joao')
print(l1)

# Restira o ultimo elemento da lista e retorna o elemento retirado
resto = l1.pop()
print(l1)
print(resto)


# Adciona a string "vitor" na ultima posicão 
l1.append('vitor')
print(l1)


del(l1[0])
print(l1)


print(l2)
print(min(l2))
print(max(l2))

