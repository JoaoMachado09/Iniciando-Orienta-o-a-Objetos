class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self.titulacao = titulacao

    def getTitulacao(self):
        return self.titulacao
    
    def setTitulacao(self, titulacao):
        self.titulacao = titulacao

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.nota1 = 0
        self.nota2 = 0
        self.matricula = 0

    def getNota1(self):
        return self.nota1
    
    def setNota1(self, nota1):
        self.nota1 = nota1

    def getNota2(self):
        return self.nota2
    
    def setNota2(self, nota2):
        self.nota2 = nota2

    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def calcularAprovacao(self):
        if self.calcular_media() >= self.limite_aprovacao():
            return "Aprovado"
        else:
            return "Reprovado"

class AlunoGraduacao(Aluno):
    def __init__(self, nome):
        super().__init__(nome)
    
    def limite_aprovacao(self):
        return 7

class AlunoEnsinoMedio(Aluno):
    def __init__(self, nome):
        super().__init__(nome)
    
    def limite_aprovacao(self):
        return 6

aluno = AlunoEnsinoMedio("Joao")
aluno.setMatricula(202324320) 
aluno.setNota1(9)
aluno.setNota2(9)

professor = Professor("Marco", "Doutor")

# Exibindo dados
print("Seus Dados:")
print("Nome:", aluno.getNome())
print("Matrícula:", aluno.getMatricula())
print("Situação:", aluno.calcularAprovacao())

print("\nSeu Professor é:")
print("Nome:", professor.getNome())
print("Titulação:", professor.getTitulacao())
