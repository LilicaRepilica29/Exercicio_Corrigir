# Questão 13 

class Conta: 
 
    def __init__(self, saldo): 
        self.saldo = saldo 
 
    def sacar(self, valor): 
        if valor <= self.saldo: 
            self.saldo -= valor 

    def exibir(self):
        return (self.saldo)
c = Conta(500) 
c.sacar(100) 
print(c.saldo)