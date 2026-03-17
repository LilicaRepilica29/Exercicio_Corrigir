# Questão 1 

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Cachorro(Animal): 
 
    def __init__(self, nome, raca): 
        super().__init__(nome)
        self.raca = raca 
 
c = Cachorro("Bolt", "Labrador") 
print(c.nome) 
print(c.raca)

#teste