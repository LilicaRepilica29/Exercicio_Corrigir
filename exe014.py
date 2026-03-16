# Questão 14 

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Gato(Animal): 
 
    def falar(self): 
        print(self.nome, "mia") 
 
g = Gato("Luna") 
g.falar() 