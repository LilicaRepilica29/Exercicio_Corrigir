# Questão 16

class Animal:
    def falar(self): 
        print("Som") 
         
class Gato(Animal): 
    def miar(self): 
        print("Miau") 
        
g = Gato() 
g.miar()