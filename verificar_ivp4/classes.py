class IPv4:
    def __init__(self, ipv4: str, mascara: int):
        self.ipv4 = ipv4.split('.')
        self.mascara = mascara
        self.ipv4Binario = []

    def numerosBinarios(self):
        aux_list = []
        for num in self.ipv4:
            num = int(num)
            bin_num = bin(num)
            bin_num = str(bin_num)[2:]
            aux_list.append(bin_num)

        for i in aux_list:
            num = ''
            for _ in range(8 - len(i)):
                num += '0'
            num = num + i
            self.ipv4Binario.append(num)

    def mascaraSubrede(self):
        mascara_subrede_bin = []

        cont = 0
        for i in range(4):
            num = ''
            for j in range(8):
                if cont < self.mascara:
                    num += '1'
                    cont += 1
                else:
                    num += '0'

            mascara_subrede_bin.append(num)

        mascara_subrede_dec = []
        for i in mascara_subrede_bin:
            num = int(i, 2)
            mascara_subrede_dec.append(str(num))

        return mascara_subrede_dec

    def quantidade_de_hosts(self):
        num = 32 - self.mascara
        hosts = (2 ** num) - 2
        return hosts

    def ips(self, tipo=''):
        num = 32 - self.mascara
        primeiro = self.ipv4Binario[-1][:8-num]
        if not tipo == 'b':
            primeiro = primeiro + ('0'*num)
        else:
            primeiro = primeiro + ('1'*num)

        primeiro_ip_lista = [self.ipv4Binario[i] for i in range(3)]
        primeiro_ip_lista.append(primeiro)

        ip_dec_lista = [str(int(i, 2)) for i in primeiro_ip_lista]

        return (ip_dec_lista, f'/{self.mascara}')

    def primeiro_e_ultimo(self):
        primeiro = self.ips()
        ultimo = self.ips('b')

        primeiro[0][-1] = str(int(primeiro[0][-1]) + 1)
        ultimo[0][-1] = str(int(ultimo[0][-1]) - 1)

        return (primeiro, ultimo)
