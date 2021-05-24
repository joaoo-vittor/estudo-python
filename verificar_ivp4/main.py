from classes import IPv4

ip = IPv4('10.20.12.45', 26)

ip.numerosBinarios()
print(f'Ip: {ip.ipv4}')
print(f'Ip em Binario: {ip.ipv4Binario}')
print(f'Mascara de Subrede: {ip.mascaraSubrede()}')
print(f'Quantidade de Hosts: {ip.quantidade_de_hosts()}')
print(f'Primeiro Ip: {ip.ips()}')
broadCast = ip.ips('b')
print(f'BroadCast: {broadCast}')
print(f'Primeiro Ip utilizavel: {ip.primeiro_e_ultimo()[0]}')
print(f'Ultimo Ip utilizavel: {ip.primeiro_e_ultimo()[1]}')
