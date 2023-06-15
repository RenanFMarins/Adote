class Pessoa:
    def __init__(self, nome, contato, tipo_preferido, preferencia):
        self.nome = nome
        self.contato = contato
        self.tipo_preferido = tipo_preferido
        self.preferencia = preferencia

class Pessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, nome, contato, tipo_preferido, preferencia):
        pessoa = Pessoa(nome, contato, tipo_preferido, preferencia)
        self.pessoas.append(pessoa)
        print("--------------------------------------------------------------")
        print("Pessoa cadastrada com sucesso!")
        print("--------------------------------------------------------------")

    def listar_pessoas(self):
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa.nome}")
            print(f"Idade: {pessoa.idade}")
            print()
