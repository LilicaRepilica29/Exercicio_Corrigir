# Questão 24

class Animal: 
    def __init__(self, nome): 
        self.nome = nome 
        
    def falar(self):
        print("Som de animal") 
        
class Cachorro(Animal): 
    def __init__(self, nome, raca): 
        super(). __init__(nome)
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
        if valor > 0 :
            self._saldo += valor 
    
    def sacar(self, valor): 
        if valor <= self._saldo: 
            self._saldo -= valor 
            
    def get_saldo(self): 
        return self._saldo 
            
class Produto: 
    def __init__(self, preco): 
        self._preco = preco 
    @property 
    def preco(self): 
        return self._preco 
    @preco.setter 
    def preco(self, valor): 
        if valor > 0 :
            self._preco = valor 
animais = [ Cachorro("Bolt", "Labrador"), Gato("Luna"), Vaca("Estrela") ]

for a in animais: 
    a.falar() 
    

conta = Conta(1000) 
conta.depositar(500) 
conta.sacar(200) 
print("Saldo:", conta.get_saldo()) 
p = Produto(100) 
p.preco = 200 
print(p.preco)



# Tarefa dos estudantes

# Peça para eles responderem:

# 1. Quantos erros existem no código? = 8.

# 2. Onde está o erro de herança? = class Cachorro.

# 3. Onde está o erro de super() ou falta dele? = Na class Cachorro,  esta faltando o super().

# 4. Onde está o erro de encapsulamento? = class Conta.

# 5. Onde está o erro de getter? = tinha alguns erros antes de iniciar o if, não tinha os ":".

# 6. Onde está o erro de property? = não estava usando "self.__" antes do atributo.

# 7. Onde está o erro de polimorfismo? = não utilizou "self." ates do nome e não tinha o "super()"