# CUSTRUIR UM NÓ
class No:
  def __init__(self, dado):
    self.dado = dado
    self.esquerda = None # MENOR
    self.direita = None # MAIOR

# ARVORE BINARIA
class ArvoreBinaria:
  # INICIALIZANDO E VERIFICANDO AS VARIAVEIS.
  def __init__(self, dado=None, no=None):
    # VERIFICA SE O NÓ JÁ EXISTE.
    if no:
      self.raiz = no
    # VERIFICA SE O ELEMENTOS FORAM PASSADOS.
    elif dado:
      no = No(dado)
      self.raiz = no
    # CASO NÃO TENHA NEM O NÓ, A RAIZ SERÁ NONE(VAZIA).
    else:
      self.raiz = None

  def altura(self, no=None):
    if no is None:
      no = self.raiz

    altura_esquera = 0
    altura_direita = 0

    if no.esquerda:
      altura_esquera = self.altura(no.esquerda)
    if no.direita:
      altura_direita = self.altura(no.direita)
      
    if altura_direita > altura_esquera:
      return altura_direita + 1
    return altura_esquera + 1

  def insere(self, valor):
    # PAI DO NOVO NÓ
    pai = None
    # RAIZ
    aux = self.raiz

    # ENQUANTO TIVERMOS UMA RAIZ.
    while(aux):
      pai = aux
      # VALOR MENOR QUE A RAIZ, É INSERIDO NA ESQUERDA.
      if valor < aux.dado:
        aux = aux.esquerda
      # VALOR MAIR QUE A RAIZ, É INSERIDO NA DIREITA.
      else:
        aux = aux.direita

    # SE NÃO TIVER O UM RAIZ, SERÁ INSERIDO O 1° VALOR DA INSERÇÃO.
    if pai is None:
      # VIRA A RAIZ DA ARVORE.
      self.raiz = No(valor)
    # FILHO MENOR QUE O PAI, É INSERIDO NA ESQUERDA.
    elif valor < pai.dado:
      pai.esquerda = No(valor)
    # FILHO MAIR QUE O PAI, É INSERIDO NA DIREITA.
    else:
      pai.direita = No(valor)

  def busca(self, valor):
    # 1° PARAM -> VALOR A SER ENCONTRADO; 2° PARAM NÓ RAIZ
    return self._busca(valor, self.raiz)

  # METODO INTERNO.
  def _busca(self, valor, no):
    # SE NÃO TIVER UM NÓ
    if no is None:
      return no
    # SE O VALOR A SER ENCONTRADO FOR IGUAL A NÓ
    if no.dado == valor:
      # RETORNA UMA SUB ARVORE A PARTIR DO NÓ BUSCADO
      return ArvoreBinaria(no)
    # SE O VALOR FOR MENOR QUE A NÓ, DESCE PELA ESQUERDA
    if valor < no.dado:
      return self._busca(valor, no.esquerda)
    return self._busca(valor, no.direita)

"""


         89
    45       99
           95  111


"""