"""
Aula 10

Web Scraping com Python

"""

import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://pt.wikipedia.org/wiki/Lista_de_partidos_pol%C3%ADticos_do_Brasil'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')
print(html)

"""
th: .headerSort

"""

conteudo = []
for content in html.find_all(attrs={"style": "font-size: 90%;"}):
    for tbody in content.find_all('tbody'):
        for th in tbody.find_all('th'):
            conteudo.append(th.text)

        for td in tbody.find_all('td'):
            conteudo.append(td.text)

# 271

dados_aux = conteudo[271:]

for index, dado in enumerate(dados_aux):
    dados_aux[index] = dado.replace('\n', '')

base_final = []
aux_arr = []
size = len(dados_aux)

cont = 7
for i in range(size):
    aux_arr.append(dados_aux[i])
    if i == cont:
        base_final.append(aux_arr)
        aux_arr = []
        cont += 8

for index, palavra in enumerate(base_final[0]):
    nome = re.match(r'^(\w\s?\.?)+|(-)', palavra)
    nome = (nome.group()).strip()
    base_final[0][index] = nome


for i in base_final:
    print(i)


with open('lista-partidos.csv', 'w+') as f:
    escreve = csv.writer(f, delimiter=',')

    for values in base_final:
        escreve.writerow(values)
