"""Documentação de uma linha
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nulla gravida aliquet maximus. Morbi non est est. Lorem 
ipsum dolor sit amet, consectetur adipiscing elit. Nulla 
facilisi. Praesent pharetra, eros et porttitor posuere, 
quam nisl tempor purus, sit amet maximus ipsum ex ac augue. 
Phasellus tincidunt nibh non ullamcorper semper. Duis sit 
amet eros tincidunt, blandit massa ut, tristique orci. 
Fusce faucibus vestibulum metus mollis condimentum. 
Phasellus faucibus, augue id placerat luctus, leo justo 
faucibus eros, sit amet lacinia elit nisi vel erat. Suspendisse 
placerat fringilla fringilla. Phasellus molestie leo sit amet 
mauris fermentum tempus. Cras consequat fringilla quam, in 
mattis est commodo eget.

Duis et tortor facilisis, tincidunt quam ut, porta nibh. Integer 
venenatis metus ut nisl vulputate, accumsan posuere tellus sollicitudin. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, 
per inceptos himenaeos. Ut a magna in sapien cursus egestas at a magna. 
Nam tincidunt arcu ut sagittis lobortis. Aenean faucibus massa felis, 
nec eleifend nulla imperdiet ac. Sed vehicula condimentum est, 
eu molestie felis congue ut. Nulla ut sagittis tortor. Aliquam sed 
mi ut ipsum varius consequat quis eu mi. Fusce nec ultricies odio, 
tempus dignissim ligula. Vestibulum ut convallis nulla. 

"""


class MinhaClasse:
    """
    Documentação da minha classe
    """

    variavel = 'valor a'

    def __init__(self, texto):
        """
        Inicializa os dados

        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto

    def soma(self, x, y):
        """
        Método de Soma

        :param x: Numero 1
        :type x: int or float
        :param y: Numero 2
        :type y: int or float

        :return: A soma de x e y
        :rtype: int or float
        """
        return x + y
