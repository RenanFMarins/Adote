from animais.cad_animais import Animais
from usuarios.cad_usuarios import Pessoas

cadastro = Animais()
cadastropessoa = Pessoas()

while True:
    print("Menu:")
    print("1. Cadastrar Animal")
    print("2. Listar Animais Cadastrados")
    print("3. Cadastrar Pessoa")
    print("4. Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        print("Você escolheu a opção Cadastrar Animal")
        nome = input("Digite o nome do animal: ")
        tipo = input("Digite o tipo do animal: ")
        cadastro.cadastrar_animal(nome, tipo)
        
    elif opcao == "2":
        print("Listar animais cadastrados")
        cadastro.listar_animais()
        
    elif opcao == "3":
        print("Você escolheu cadastrar pessoa")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cadastropessoa.cadastrar_pessoa(nome, idade)
        
    elif opcao == "4":
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
