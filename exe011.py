# Questão 11 

class Produto: 
 
    def __init__(self, preco): 
        self.__preco = preco 
 
p = Produto(100) 
p.__preco = -200 
print(p.__preco) 

 