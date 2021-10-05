import random


class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.curso = curso

    def imprimi(self):
        return f"Aluno: {self.nome}, CPF: {self.cpf} - Matricula - {self.matricula} - Curso: {self.curso}"

if name == "main":
    nome_aluno = input('Digite seu nome: ')
    cpf_aluno = input('Digite seu cpf: ')
    curso_option = int(input(
        "Selecione seu curso: \n 1 - ADS \n 2 - Tec. Informática \n"
        )
    )
    cursos = {
        1: 'ADS',
        2: 'Tec. Informática'
    }

    matricula = random.randint(0,2000)

    aluno = Aluno(nome_aluno, cpf_aluno, matricula, cursos[curso_option])

    print(aluno)

