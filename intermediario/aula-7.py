"""
Aula 7

List Comprehension

"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [x + 1 for x in l1]
print(ex1)

print()
ex2 = [x * 2 for x in l1]
print(ex2)

print()
ex3 = [(x, y) for x in l1 for y in range(3)]
print(ex3)

ex4 = [x for x in l1 if x % 2 == 0]
print(ex4)
