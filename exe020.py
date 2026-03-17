# Questão 20

class Animal: 
    def __init__(self, nome): 
        self.nome = nome 
        
    def falar(self): 
        print("Som") 
        
class Cachorro(Animal): 
    
    def __init__(self, nome, raca): 
        super().__init__(nome) 
        self.raca = raca 
        
    def falar(self): 
        super().falar() 
        print(f"{self.nome}...Au au...") 
        
animais = [ Cachorro("Bolt", "Labrador"), Animal("Bicho") ]

for a in animais: 
    a.falar()