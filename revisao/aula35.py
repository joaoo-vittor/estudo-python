"""
Aula 35

Problema dos parâmetros mutáveis em funções

"""

def lista_de_clientes(clientes_iteraveis, lista=None):
  lista = [] if lista is None else None
  lista.extend(clientes_iteraveis)
  return lista

clientes1 = lista_de_clientes(['joao', 'otavio', 'manu'])
clientes2 = lista_de_clientes(['Jonas', 'Sofia', 'Maria'])
clientes3 = lista_de_clientes(['Jose'])

print(clientes1)
print(clientes2)
