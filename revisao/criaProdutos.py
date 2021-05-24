import random as rdm

nomes = [ 'Alexandre', 'Eduardo', 'Henrique', 'Murilo', 'Theo', 
  'Alícia','Carolina', 'Fernanda', 'Joana	Malu', 'Nicole'
]

def criaProduto():
  with open('produtos.py', 'w') as file:
    file.write('produto = [\n')
    aux = ''
    for i in range(1, 11):
      preco = rdm.random() * 100
      aux += '\t{"nome": "p'+ str(i) +'" ,"preco": '+ str(round(preco, 2)) +' },\n' 
    file.write(aux)
    file.write(']\n\n')

    criaNomes(file)


def criaNomes(file):
  file.write('pessoas = [\n')
  aux = ''
  for nome in nomes:
    idade = rdm.randint(12, 80)
    aux += '\t{"nome": "'+ nome +'" ,"idade": '+ str(idade) +' },\n' 
  file.write(aux)
  file.write(']\n\n')

criaProduto()
