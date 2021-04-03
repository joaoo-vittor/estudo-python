"""
Aula 14

 Openpyxl - Planilhas do Excel em Python

"""
import openpyxl

pedidos = openpyxl.load_workbook('./excel/pedidos.xlsx')

nome_planinhas = pedidos.sheetnames
planinha1 = pedidos['Página1']

"""
for campo in planinha1['b']:
    if campo.value is None:
        print(campo.value)
       
"""

for linha in planinha1:
    if linha[0].value is not None:
        print(linha[0].value, '\t', linha[1].value, '\t', linha[2].value)
