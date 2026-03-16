# Questão 3 

class Pessoa: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Professor(Pessoa): 
 
    def __init__(self, nome, disciplina): 
        super().__init__(nome) 
        self.disciplina = disciplina 
 
p = Professor("Ana", "Programação") 
print(p.nome) 
print(p.disciplina) 