"""
Aula 11

split and join

"""

string_1 = 'Lorem ipsum dolor sit amet'
string_2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

new_string_1 = string_1.split(' ')
new_string_2 = string_2.split(',')

print(new_string_1)
print(new_string_2)

join_new_str_1 = ' '.join(new_string_1)
join_new_str_2 = ','.join(new_string_2)

print(join_new_str_1)
print(join_new_str_2)
