# Questão 18
class Animal: 
    def falar(self): 
        print("Som") 
        
class Cachorro(Animal): 
    def falar(self): 
        print("Au au") 
                
class Gato(Animal):  
    def falar(self): 
        print("miau miau...") 

                
animais = [Cachorro(), Gato()] 
for a in animais: a.falar()