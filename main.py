from animais.cad_animais import Animais

cadastro = Animais()

while True:
    print("Menu:")
    print("1. Cadastrar Animal")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        print("Você escolheu a opção Cadastrar Animal")
        nome = input("Digite o nome do animal: ")
        tipo = input("Digite o tipo do animal: ")

        cadastro.cadastrar_animal(nome, tipo)
    elif opcao == "2":
        print("Você escolheu a opção 2")
    elif opcao == "3":
        print("Você escolheu a opção 3")
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
