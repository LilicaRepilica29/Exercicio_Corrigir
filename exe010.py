# Questão 10 

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 

    def falar(self): 
        print(f"{self.nome}  Au au") 
class Cachorro(Animal): 
 
    def __init__(self, nome): 
        super().__init__(nome) 
 
    
animais = [ 
Cachorro("Bolt"), 
Animal("Bicho") 
] 
 
for a in animais: 
    a.falar() 

