# Questão 17

class Conta: 
    def __init__(self, saldo): 
        self._saldo = saldo 
    def set_saldo(self, valor): 
        if valor >= 0: 
            self._saldo = valor
        else:
            print("Valor invalido!")
                
    def get_saldo(self): 
        return self._saldo        

c = Conta(100) 
c.set_saldo(-50) 
print(c.get_saldo())
