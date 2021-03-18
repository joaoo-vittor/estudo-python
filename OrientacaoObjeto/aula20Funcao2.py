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

variavel = 'valor'


def soma():
    """
    Soma x e y

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return 1


def multiplica(x, y, z=None):
    """Multiplica x, y, z

    multiplica x, y e z. O programador pode omitir a varivel z caso não
    necessite de usa-lá

    :param x: Numero 1
    :type x: int or float
    :param y: Numero 2
    :type y: int or float
    :param z: Numero 3 (optional)
    :type z: int or float

    :return: A mutiplicação entre x, y e z
    :rtype: int or float
    """

    if z:
        return x * y
    else:
        return x * y * z


variavel1 = 1
variavel2 = 2
variavel3 = 3
