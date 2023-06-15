class Animais:
    def __init__(self):
        self.animais = {}
    
    def cadastrar_animal(self, tipo, nome, idade_aproximada, cor, porte, particularidade):
        animal = {
            'nome': nome,
            'idade_aproximada': idade_aproximada,
            'cor': cor,
            'porte': porte,
            'particularidade': particularidade
        }
        
        if tipo in self.animais:
             self.animais[tipo].append(animal)
        else:
            self.animais[tipo] = [animal]
        print("Animal cadastrado com sucesso!")
        
    def listar_animais(self):
        for tipo, lista_animais in self.animais.items():
            print(f"Tipo: {tipo}")
            
        for animal in lista_animais:
            print("Nome:", animal['nome'])
            print("Idade Aproximada:", animal['idade_aproximada'])
            print("Cor:", animal['cor'])
            print("Porte:", animal['porte'])
            print("Particularidade:", animal['particularidade'])
            print()
