def geraArquivo(nome, extencao, inicio, fim):
  for index in range(inicio, fim+1):
    nomeArq = nome + str(index) + extencao
    with open(nomeArq, 'w') as file:
      aux = '"""\nAula ' + str(index) + '\n"""'
      file.write(aux)

geraArquivo('aula', '.py', 27, 35)
