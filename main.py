while True:  # laço para executar tudo que estiver dentro desse bloco continuamente

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
    print()

    if opcao == 1:

        print("========================================")
        print("          NOVA SOLICITAÇÃO              ")
        print("========================================")
        print()

        solicitante = input("Informe o nome do solicitante: ")
        print()

        print("Selecione o setor responsável:")
        print()
        print("1 - Controladoria")
        print("2 - Recursos Humanos")
        print()

        setor = int(input("Escolha uma opção: "))
        print()

        if setor == 1:

            nome_setor = "Controladoria"

            print("CONTROLADORIA")
            print()
            print("1 - Comprovante de pagamento")
            print("2 - Confirmação de recebimento de cliente")
            print("3 - Relatório para diretoria/gerência")
            print("4 - Dados cadastrais")
            print("5 - Outros")
            print()

            tipo = int(input("Escolha o tipo de solicitação: "))

            if tipo == 1:
                tipo_solicitacao = "Comprovante de pagamento"

            elif tipo == 2:
                tipo_solicitacao = "Confirmação de recebimento de cliente"

            elif tipo == 3:
                tipo_solicitacao = "Relatório para diretoria/gerência"

            elif tipo == 4:
                tipo_solicitacao = "Dados cadastrais"

            elif tipo == 5:
                tipo_solicitacao = "Outros"

            else:
                tipo_solicitacao = "Tipo inválido"

        elif setor == 2:

            nome_setor = "Recursos Humanos"

            print("RECURSOS HUMANOS")
            print()
            print("1 - Holerite")
            print("2 - Informe de rendimentos")
            print("3 - Documentos de plano de saúde")
            print("4 - Calendário de exames médicos periódicos")
            print("5 - Outros")
            print()

            tipo = int(input("Escolha o tipo de solicitação: "))

            if tipo == 1:
                tipo_solicitacao = "Holerite"

            elif tipo == 2:
                tipo_solicitacao = "Informe de rendimentos"

            elif tipo == 3:
                tipo_solicitacao = "Documentos de plano de saúde"

            elif tipo == 4:
                tipo_solicitacao = "Calendário de exames médicos periódicos"

            elif tipo == 5:
                tipo_solicitacao = "Outros"

            else:
                tipo_solicitacao = "Tipo inválido"

        else:
            print("Setor inválido.")
            continue

        descricao = input("Descreva a solicitação: ")
        print()

        print("========================================")
        print("        RESUMO DA SOLICITAÇÃO")
        print("========================================")
        print()

        print("Solicitante...:", solicitante)
        print("Setor.........:", nome_setor)
        print("Tipo..........:", tipo_solicitacao)
        print("Descrição.....:", descricao)
        print()

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
        break  # interrompe o laço while True

    else:
        print("Opção inválida.")

    print()