# Questão 1 
from rich import print #py -m pip install rich
from rich.panel import Panel

class Animal: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Cachorro(Animal): 
 
    def __init__(self, nome, raca): 
        super().__init__(nome)
        self.raca = raca 
    def analisar(self):
        conteudo = (f"O cahorro se chama {self.nome} e sua raça é {self.raca}")
        painel = Panel(conteudo, title=self.nome)
        print(painel)
c = Cachorro("Bolt", "Labrador") 
print(c.nome) 
print(c.raca)

#teste