# Questão 2 
class Conta: 
 
    def __init__(self, saldo): 
        self._saldo = saldo 
 
    def sacar(self, valor): 
        if valor <= self._saldo: 
            self._saldo -= valor 
 
conta = Conta(1000) 
print(conta._saldo) 
conta.sacar(700)
print(conta._saldo)