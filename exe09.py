# Questão 9 

class Pessoa: 
 
    def __init__(self, nome): 
        self.nome = nome 
 
class Aluno(Pessoa): 
 
    def estudar(self): 
        print(self.nome, "está estudando") 
 
a = Aluno("Lucas") 
a.estudar() 