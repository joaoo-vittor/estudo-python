"""
Aula 2

Datetime - Trabalhando com data e hora em Python

https://docs.python.org/2/library/datetime.html

"""
from datetime import datetime, timedelta

data = datetime(2021, 3, 21, 16, 34, 59)

print(data.strftime('%d/%m/%Y %H:%M:%S'))


print('\n', '#'*20, '\n')


data1 = datetime.strptime('21/03/2021', '%d/%m/%Y')

print(data1)
print('timestamp: ', data1.timestamp())


print('\n', '#'*20, '\n')


data2 = datetime.fromtimestamp(1616295600.0)

print(data2)


print('\n', '#'*20, '\n')

data3 = datetime.strptime('21/03/2021 17:32:00', '%d/%m/%Y %H:%M:%S')

data3 = data3 + timedelta(days=5)
data3 = data3 + timedelta(seconds=2*60*60)

print(data3.strftime('%d/%m/%Y %H:%M:%S'))


print('\n', '#'*20, '\n')


data4 = datetime.strptime('21/03/2021 17:32:00', '%d/%m/%Y %H:%M:%S')
data5 = datetime.strptime('28/03/2021 11:32:00', '%d/%m/%Y %H:%M:%S')

dif = data4 - data5
dif = abs(dif)
print(dif)
print(dif.seconds)
print(data5 > data4)
