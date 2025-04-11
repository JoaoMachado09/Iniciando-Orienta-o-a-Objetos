class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        
    def set_nome(self, nome):
        self.nome = nome
    def get_nome(self):
        return self.nome
    

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.titulacao = ""
    
    def set_titulacao(self, titulacao):
        self.titulacao = titulacao
    def get_titulacao(self):
        return self.titulacao
    
    
    
class Aluno(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)
        self.nota1 = 0
        self.nota2 = 0
        self.matricula = 0
           
    def set_nota1(self, nota1):
        self.nota1 = nota1
    def get_nota1(self):
        return self.nota1
    
    def set_nota2(self, nota2):
        self.nota2 = nota2
    def get_nota2(self):
        return self.nota2
    
    def calcular_media(self):
        return ( self.nota1 + self.nota2 )/ 2



class AlunoGraduacao(Aluno):
    def __init__(self, nome):
        Aluno.__init__(self, nome)

    def calcularAprovacao(self):
        if self.calcular_media >= 7:
            print('aprovado')
        else:
            print("reprovado")


class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome):
        Aluno.__init__(self, nome)

    def calcularAprovacao(self):
        if self.calcular_media >= 6:
            return 'aprovado'
        else:
            return "reprovado"



aluno = AlunoGraduacao("joao")
aluno.set_nota1(3)
aluno.set_nota2(4)
aluno.calcularAprovacao()