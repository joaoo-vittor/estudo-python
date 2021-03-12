"""
Aula 6

sets

add -> adiciona
update -> atualiza OBS: recebe um iteravel
clear -> limpa
discard -> remove elemento
union -> | -> une
intersection -> & -> elementos dos dois sets
difference -> - -> elementos do set da esquerda
symmetric_difference -> ^ -> elementos que estão nos dois sets, mas não em ambos

OBS: não aceita elementos duplicados

"""

# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# s1 = set()
# s1.add(1)
# s1.add(2)
# print(s1)
# s1.discard(2)
# print(s1)
# # s1.clear()
# # print(s1)
# s1.update('python')
# print(s1)

# l1 = [1, 2, 1, 2, 2, 2, 3, 5, 4, 6, 6, 6, 7, 8, 9, 9, 9, 9]
# l1 = set(l1)
# l1 = list(l1)
# print(l1)


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}

s3 = s1 | s2
print('União: ')
print(s3)

s4 = s1 & s2
print('Intersecção: ')
print(s4)


s5 = s1 - s2
print('Diferença: ')
print(s5)

s6 = s1 ^ s2
print('Diferença Simetrica: ')
print(s6)
