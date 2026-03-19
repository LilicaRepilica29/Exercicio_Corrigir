# Questão 7 

class Conta: 
 
    def __init__(self, saldo): 
        self.__saldo = saldo 
 
    def depositar(self, valor): 
        if valor > 0: 
            self.__saldo += valor 
        else:
            return ("Valor invalido!")
    def get_saldo(self):
        return (self.__saldo)

    
conta = Conta(1000) 
print(conta.depositar(-500))
print(conta.get_saldo()) 