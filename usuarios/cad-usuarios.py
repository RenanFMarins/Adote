class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")
