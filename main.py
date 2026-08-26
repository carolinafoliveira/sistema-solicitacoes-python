while True: #laço para executar tudo que estiver dentro desse bloco continuamente.

    print("========================================")
    print("    SISTEMA DE SOLICITAÇÕES INTERNAS    ")
    print("========================================")
    print()

    print("1 - Nova solicitação")
    print("2 - Listar solicitações")
    print("3 - Consultar solicitação")
    print("4 - Alterar status")
    print("5 - Finalizar solicitação")
    print("6 - Relatórios")
    print("0 - Sair")
    print()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Nova solicitação")

    elif opcao == 2:
        print("Listar solicitações")

    elif opcao == 3:
        print("Consultar solicitação")

    elif opcao == 4:
        print("Alterar status")

    elif opcao == 5:
        print("Finalizar solicitação")

    elif opcao == 6:
        print("Relatórios")

    elif opcao == 0:
        print("Encerrando o sistema...")
        break # para interromper o laço True que é infinito
    else:
        print("Opção inválida.")
        
    print()
    