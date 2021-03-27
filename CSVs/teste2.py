import csv
import random as rdm


def criarArqCsv(linhas, colunas):
    with open('ex6.csv', 'w+') as file:
        escreve = csv.writer(file, delimiter=',')

        escreve.writerow(
            colunas
        )

        size = len(colunas)
        values = popula(linhas, size)
        for content in values:
            escreve.writerow(content)


def popula(linhas, size_colunas):
    letras = ['E', 'X', 'L', 'O', 'Q', 'M', 'J', 'F', 'K', 'H']
    arr_externo = []
    for i in range(linhas):
        arr_interno = []
        for j in range(size_colunas):
            num = (rdm.random() * 10) - 6
            arr_interno.append(num)
        num_letra = rdm.randint(0, size_colunas)
        arr_interno[size_colunas - 1] = letras[num_letra]
        arr_externo.append(arr_interno)
    return arr_externo


criarArqCsv(10000, ['one', 'two', 'three', 'four', 'key'])

# result = popula(10, 5)
# for arr in result:
#     print(arr)
