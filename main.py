from animais.cad_animais import Animais
from usuarios.cad_usuarios import Pessoas

cadastro = Animais()
cadastropessoa = Pessoas()

while True:
    print("Menu:")
    print("1. Cadastrar Animal")
    print("2. Listar tipos de Animais")
    print("3. Cadastrar Pessoa para Adoção")
    print("4. Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        print("Você escolheu a opção Cadastrar Animal")
        
        tipo = input("Digite o tipo do animal: ")
        nome = input("Digite o nome do animal: ")
        idade_aproximada = input("Digite a idade aproximada do animal: ")
        cor = input("Digite a cor do animal: ")
        porte = input("Digite o porte do animal: ")
        particularidade = input("Digite a particularidade do animal: ")
        
        cadastro.cadastrar_animal(tipo, nome, idade_aproximada, cor, porte, particularidade)
        
    elif opcao == "2":
        print("--------------------------------------------------------------")
        print("Tipos animais cadastrados")
        print("--------------------------------------------------------------")
        cadastro.listar_tipos_animais_ordenar()
        
    elif opcao == "3":
        print("Você escolheu a opção Cadastrar Pessoa para Adoção")
        nome = input("Digite o nome da pessoa: ")
        contato = input("Digite o contato da pessoa: ")
        tipo_preferido = input("Digite o tipo de animal preferido da pessoa: ")
        preferencia= input("digite suas preferencias: ")

        cadastropessoa.cadastrar_pessoa(nome, contato, tipo_preferido, preferencia)
        
        print("Tipos animais cadastrados:")
        cadastro.listar_tipos_animais()
        
    elif opcao == "4":
        print("Você escolheu listar pessoas cadastradas")
        
        cadastropessoa.listar_pessoas()

    elif opcao == "5":
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
