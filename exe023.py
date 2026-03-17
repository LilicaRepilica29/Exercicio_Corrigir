# Questão 23

class Produto:

    def __init__(self, preco):
        self._preco = preco
        
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,valor):
        if valor > 0:
            self._preco = valor

p = Produto(50)
print(p.preco)

