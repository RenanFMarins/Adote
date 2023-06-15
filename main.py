from animais.cad_animais import Animais
from usuarios.cad_usuarios import Pessoas

cadastro = Animais()
cadastropessoa = Pessoas()

while True:
    print("Menu:")
    print("1. Cadastrar Animal")
    print("2. Listar Animais Cadastrados")
    print("3. Cadastrar Pessoa")
    print("4. listar pessoas cadastradas")
    print("5. Sair")
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
        print("Listar animais cadastrados")
        cadastro.listar_animais()
        
    elif opcao == "3":
        print("Você escolheu cadastrar pessoa")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        
        cadastropessoa.cadastrar_pessoa(nome, idade)
        
    elif opcao == "4":
        print("Você escolheu listar pessoas cadastradas")
        
        cadastropessoa.listar_pessoas()

    elif opcao == "5":
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
