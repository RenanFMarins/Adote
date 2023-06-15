class Animais:
    def __init__(self):
        self.animais = {}
   
    def linha():
    print('-='*30)
    
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
        
    def listar_tipos_animais(self):
        print("Tipos de animais cadastrados:")
        tipos = list(self.animais.keys())
        for i, tipo in enumerate(tipos):
            print(f"{i + 1}. {tipo}")
        print("0. Adicionar um novo tipo de animal")
        print()
        escolha = input("Digite o número do tipo desejado ou 0 para adicionar um novo tipo: ")
        escolha = int(escolha)

        if escolha == 0:
            novo_tipo = input("Digite o nome do novo tipo de animal: ")

            if novo_tipo in self.animais:
                print(f"O tipo de animal '{novo_tipo}' já existe.")
            else:
                self.animais[novo_tipo] = []
                print(f"Tipo de animal '{novo_tipo}' adicionado com sucesso!")
        elif 1 <= escolha <= len(tipos):
            tipo_escolhido = tipos[escolha - 1]
            animais_tipo_escolhido = self.animais[tipo_escolhido]

            animais_tipo_escolhido_ordenados = sorted(animais_tipo_escolhido, key=lambda animal: int(animal['idade_aproximada']))

            print(f"Animais do tipo '{tipo_escolhido}':")
            linha()
            for animal in animais_tipo_escolhido_ordenados:
                print("Nome:", animal['nome'])
                print("Idade Aproximada:", animal['idade_aproximada'])
                print("Cor:", animal['cor'])
                print("Porte:", animal['porte'])
                print("Particularidade:", animal['particularidade'])
            linha()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
