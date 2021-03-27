"""
Aula 8

String - Template

"""
from string import Template
from datetime import datetime

with open('aula8.html', 'r') as file:
    template = Template(file.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='João Vitor', data=data_atual)
    corpo_msg = template.safe_substitute(nome='João Vitor', data=data_atual)

print(corpo_msg)
