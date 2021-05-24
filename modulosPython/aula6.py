"""
Aula 6

JSON - JavaScript Object Notation

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
import aula6Dados as dados
import json as js

lista = [1, 2, 3, 4, 5, 6]

dados_json = js.dumps(lista)

print(dados_json)
print(type(dados_json))


print('\n', '#'*20, '\n')


dicionario_json = js.dumps(dados.clientes_dicionario, indent=4)
print(dicionario_json)


print('\n', '#'*20, '\n')

dicionario = js.loads(dados.clientes_json)

print(type(dicionario))

for key, value in dicionario.items():
    print(key, value)


# with open('aula6.json', 'w') as file:
#     js.dump(dados.clientes_dicionario, file, indent=4)


print('\n', '#'*20, '\n')


with open('aula6.json', 'r') as file:
    dado_json = js.load(file)


for key, value in dado_json.items():
    print(key, value)
