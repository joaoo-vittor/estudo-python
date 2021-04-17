"""
Aula 22



"""

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = sum([preco for _ ,preco in carrinho])

print(total)
