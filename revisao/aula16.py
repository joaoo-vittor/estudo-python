"""
Aula 16

Sets - Conjuntos

-> add (Adiciona)
-> update (Atualiza)
-> clear
-> discard

-> union => |  (une)
-> intersection => &  (Todos os elementos presentes nos dois sets)
-> diference => -   (Elementos apenas no set da esquerda)
-> symmetric_difference => ^  (Elementos que estão nos dois sets, mas não em ambos)

"""
# Apenas elementos imutaveis

s1 = { 1, 2, 3, 4, 5, 6 }

print(s1)

s2 = set()

s2.update('python')

print(s2)


s3 = { 1,2,3,4,5 }
s4 = { 1,2,3,4,5,6 }

s5 = s3 | s4
print(s5)

s5 = s3 & s4
print(s5)

s5 = s4 - s3
print(s5)

s5 = s4 ^ s3
print(s5)

s5 = s3 ^ s4
print(s5)




