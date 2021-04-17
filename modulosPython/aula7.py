"""
Aula 7

CSV - Comma Separated Values

"""
import csv

with open('aula7.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    dados = [x for x in csv.DictReader(arquivo)]

    # next(dados)  # pula a primeira linha
    for dado in dados:
        print(dado['Nome'], dado['Sobrenome'],
              dado['E-mail'], dado['Telefone'])


with open('aula7Dois.csv', 'w+') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    print(chaves)

    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )
