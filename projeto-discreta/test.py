from ArvoreBinariaBusca import ArvoreBinaria
from geraCPF import lista_cpf

def inserir(lista):
  arvore = ArvoreBinaria()
  for cpf in lista:
    arvore.insere(cpf)
  return arvore


# print(inserir(lista_cpf))


print("\n-------------------------------------\n")
print("CPF's encontrados:")

print("\n-------------------------------------\n")

bst = inserir(lista_cpf)

print("Altura da arvore: ", bst.altura())

print("\n-------------------------------------\n")


items = [24854458002, 92518217633, 96313416902,  96313416908, 92518217677]
for item in items:
  resp = bst.busca(item)
  if resp is None:
    print(item, 'não encontrado.')
  else:
    print(item, 'encontrado.')