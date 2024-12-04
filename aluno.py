class Aluno:

    def __init__(self, nome, sobrenome, nota):
        
        if nota < 0 or nota > 10:
            
            raise ValueError("A nota deve estar entre 0 e 10.")

        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        
        return f'Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}'
