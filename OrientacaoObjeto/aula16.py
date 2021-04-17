"""
Aula 16

Sobrecarga de operadores - Python Orientado a Objetos

No python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuario.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão

"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y

    def __add__(self, otherObj):
        novo_x = self.x + otherObj.x
        novo_y = self.y + otherObj.y
        return Retangulo(novo_x, novo_y)

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __lt__(self, otherObj):
        a1 = self.getArea()
        a2 = otherObj.getArea()

        if a1 < a2:
            return True
        return False

    def __gt__(self, otherObj):
        a1 = self.getArea()
        a2 = otherObj.getArea()

        if a1 > a2:
            return True
        return False

    def __eq__(self, otherObj):
        if self.x == otherObj.x and self.y == otherObj.y:
            return True
        return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 30)
r4 = Retangulo(10, 30)

r3 = r1 + r2

# print(r3)
print(r1 > r3)
print(r2 == r4)
