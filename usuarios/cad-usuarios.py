class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, nome, idade):
        pessoa = Pessoa(nome, idade)
        self.pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    def listar_pessoas(self):
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa.nome}")
            print(f"Idade: {pessoa.idade}")
            print()
