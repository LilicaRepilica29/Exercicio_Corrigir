# Questão 21
class Animal:

    def __init__(self, nome): 
        self.nome = nome 
        
    def falar(self): 
        print("Som de animal") 
        
class Cachorro(Animal): 
    def __init__(self, nome, raca): 
        super().__init__(nome) 
        self.raca = raca 
        
    def falar(self): 
        print(self.nome, "late") 
        
class Gato(Animal): 
    def falar(self): 
        print(self.nome, "mia") 
        
class Vaca(Animal): 
    def falar(self): 
        print(self.nome, "faz muuu")

class Conta: 
    def __init__(self, saldo): 
        self._saldo = saldo 
        
    def depositar(self, valor): 
         if valor > 0: 
            self._saldo += valor 
        
    def sacar(self, valor): 
        if valor <= self._saldo: 
            self._saldo -= valor 
            
    def get_saldo(self): 
         return self._saldo 
     
animais = [ Cachorro("Bolt", "Labrador"), Gato("Luna"), Vaca("Estrela") ] 
for a in animais: a.falar() 
conta = Conta(1000) 
conta.depositar(500) 
conta.sacar(200) 
print("Saldo:", conta.get_saldo()) 
conta.depositar(500)
conta.sacar(200)
print("Saldo:", conta.get_saldo())