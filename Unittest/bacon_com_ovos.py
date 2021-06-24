"""
1 - Receber um numero inteiro

2 - Saber se o numero é multiplo de 3 e 5:
    Bacon com ovos

3 - Saber se o numero é multiplo de 3:
    Bacon

4 - Saber se o numero e multiplo de 5:
    Ovos

5 - Saber se o numero não é multiplo de 3 e 5:
    Passar fome
"""


def bacon_com_ovos(num):
    assert isinstance(num, int), '"num" deve ser int.'

    if num % 3 == 0 and num % 5 == 0:
        return 'Bacon com ovos'

    if num % 3 == 0:
        return 'Bacon'

    if num % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
