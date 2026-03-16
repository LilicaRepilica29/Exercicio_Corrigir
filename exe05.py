# Questão 5 

class Produto: 
 
    def __init__(self, preco): 
        self.__preco = preco 
 
    def set_preco(self, valor): 
        if valor > 0: 
            self.__preco = valor 
 
    def get_preco(self): 
        return self.__preco 
 
p = Produto(50) 
p.set_preco(100) 
print(p.get_preco()) 