"""
Aula 12

Funçoes Anonimas -> Expressões Lambda

"""

def mult(n1, n2):
  return n1 * n2

# print(mult(3, 5))

lambdaMult = lambda x, y: x * y

# print(lambdaMult(3, 5))

listaProd = [
  ['p1', 12],
  ['p2', 62],
  ['p3', 27],
  ['p4', 8],
  ['p5', 2]
]

def itemProd(item):
  return item[1]

print(listaProd)

print(sorted(listaProd, key=lambda item: item[1]))

# listaProd.sort(key=itemProd)
listaProd.sort(key= lambda item: item[1])
print(listaProd)

listaProd.sort(key= lambda item: item[1], reverse= True)
print(listaProd)
