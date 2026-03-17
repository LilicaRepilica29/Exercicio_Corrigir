# Questão 15

class Pessoa: 
    def __init__(self, nome): 
        self.nome = nome 
        
class Professor(Pessoa):
    def ensinar(self): 
        print(self.nome, "ensina") 
        
prof = Professor("Carlos")
prof.ensinar()