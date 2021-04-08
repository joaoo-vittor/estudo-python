def geraArquivo(nome, extencao, inicio, fim):
    for index in range(inicio, fim+1):
        nomeArq = nome + str(index) + extencao
        with open(nomeArq, 'w') as file:
            aux = '"""\nAula ' + str(index) + '\n"""'
            file.write(aux)


def geraSnippet(n):
    with open('snippetPython.txt', 'w') as file:
        aux = ''
        for i in range(1, n):
            aux += '"SnippetPY n ' + str(i) + '": {\n'
            aux += '\t"prefix": "",\n'
            aux += '\t"body": [\n'
            aux += '\t\t""\n'
            aux += '\t],\n'
            aux += '},\n'
        file.write(aux)


geraArquivo('aula', '.py', 1, 5)
# geraSnippet(15)
