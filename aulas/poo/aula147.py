# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y): # construtor
        self.x = x
        self.y = y

    def __repr__(self): # representação oficial
        class_name = type(self).__name__ 
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other): # self + other
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other): # self > other
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__': # Testes
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2 # Ponto(10, 6)
    print(p3) # Ponto(x=10, y=6)
    print('P1 é maior que p2', p1 > p2) # False
    print('P2 é maior que p1', p2 > p1) # True