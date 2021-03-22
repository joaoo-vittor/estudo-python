"""
Aula 3

Datetime #2 - Datas em português

https://docs.python.org/2/library/datetime.html

"""
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.now()

formatacao1 = data.strftime('%A %d, de %B de %Y')
formatacao2 = data.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

print('\n', '#'*20, '\n')

mes_atual = int(data.strftime('%m'))

print(mes_atual, mdays[mes_atual])
