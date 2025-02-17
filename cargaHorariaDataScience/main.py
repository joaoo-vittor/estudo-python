from bs4 import BeautifulSoup
import requests as req
import math

test = """Adobe XD
Blender
Desenho básico
Design de Jogos
Design Gráfico
Edição de vídeo
Estatística para UX Research
Figma 
Fotografia 
HQ - Narrativa Sequencial
Identidade Visual 
Identidade Visual com softwares gratuitos 
Ilustração Publicitária no Photoshop 
InDesign 
Motion Design
Osteologia ZBrush 
Pesquisas qualitativas para UX Research 
Pintura Digital no Photoshop 
Produção com Photoshop
Produção de vídeo no Premiere 
Produção Gráfica com Illustrator
Props para games 
Sketch 
Tratamento de Imagem 
Unreal Engine 
UX Design 
UX Research 
"""

aux_list = []
aux_name = ''
for i in list(test):
    if i != '\n':
        aux_name += i
    else:
        aux_list.append(aux_name.strip())
        aux_name = ''

# print(aux_list)


modulos = ['sql', 'data-science', 'data-visualization',
           'machine-learning', 'business-intelligence',
           'nosql', 'matematica', 'estatistica']

cargas = {}


html = req.get(url='https://www.alura.com.br/cursos-online-design-ux')

# print(html.text)

"""
with open('./alura.html', 'r') as f:
    html = BeautifulSoup(f, 'html.parser')
    # print(html)
    for i in modulos:
        arr_curso = []
        arr_carga = []
        aux_mod = ''
        for content in html.find_all(attrs={'id': i}):
            # print(content)
            for el in content.find(attrs={'class': 'subcategoria__nome'}):
                aux_mod = el
                cargas[str(el)] = []
            for el2 in content.find_all(attrs={'class': 'card-curso__nome'}):
                arr = []
                for aux in el2.text.split(' '):
                    if aux != '':
                        arr.append(aux.replace('\n', ''))
                arr_curso.append(' '.join(arr))
            for el3 in content.find_all(attrs={'class': 'card-curso__carga'}):
                arr_carga.append(el3.text.strip())

        if len(arr_carga) == len(arr_curso):
            for i in zip(arr_curso, arr_carga):
                cargas[aux_mod].append(i)
"""

html = BeautifulSoup(html.text, 'html.parser')
# print(html)
for i in aux_list:
    arr_curso = []
    arr_carga = []
    aux_mod = ''
    for content in html.find_all(attrs={'id': i}):
        # print(content)
        for el in content.find(attrs={'class': 'subcategoria__nome'}):
            aux_mod = el
            cargas[str(el)] = []
        for el2 in content.find_all(attrs={'class': 'card-curso__nome'}):
            arr = []
            for aux in el2.text.split(' '):
                if aux != '':
                    arr.append(aux.replace('\n', ''))
            arr_curso.append(' '.join(arr))
        for el3 in content.find_all(attrs={'class': 'card-curso__carga'}):
            arr_carga.append(el3.text.strip())

    if len(arr_carga) == len(arr_curso):
        for i in zip(arr_curso, arr_carga):
            cargas[aux_mod].append(i)

horas_estudo_dia = float(input('Quantas Horas de estudo por dia: '))
aux_total = 0
for i in cargas.keys():
    total_carga = 0
    print('-', i)
    for j in cargas[i]:
        aux_carga = 0
        total_carga += int(j[1].replace('h', ''))
        aux_carga = int(j[1].replace('h', ''))
        print('  └─', j[0], '-', j[1])
        aux = 0
        hora = 0
        for k in range(int((aux_carga // horas_estudo_dia)+1)):
            hora += horas_estudo_dia

            if hora <= aux_carga:
                print(
                    f'      └─ Dia n°{k+1} carga horaria do dia é {horas_estudo_dia}hrs.')
            else:
                hora = aux_carga - (hora - horas_estudo_dia)
                if hora != 0:
                    print(
                        f'      └─ Dia n°{k+1} carga horaria do dia é {hora}hrs.')

    print(f'  └─ Carga Horaria Total de {i} é {total_carga} horas')
    print(
        f'  └─ Quantidade de dia para {horas_estudo_dia} horas de estudo de {i} é {math.ceil(total_carga/horas_estudo_dia)} dias.')
    aux_total += math.ceil(total_carga/horas_estudo_dia)

print(f'\n\n  ------- Para {horas_estudo_dia}hrs de estudo -------\n')
print(
    f'  └─ Quantidade de dia para {horas_estudo_dia} horas de estudo, para todos os cursos é {aux_total} dias.\n')
