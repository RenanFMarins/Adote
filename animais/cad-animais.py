class Animais:
    def __init__(self):
        self.animais = {}
    
    def cadastrar_animal(self, tipo, nome):
        if tipo in self.animais:
            self.animais[tipo].append(nome)
        else:
            self.animais[tipo] = [nome]
        print("Animal cadastrado com sucesso!")
        
    def listar_animais(self):
        for tipo, lista_animais in self.animais.items():
            print(f"Tipo: {tipo}")
            print("Animais: ", end="")
            print(*lista_animais, sep=", ")
            print()
