import json

# Tenta abrir o arquivo onde ficam salvas as solicitações.
# Se o arquivo existir, os dados são carregados para a lista "solicitacoes".
try:
    with open("solicitacoes.json", "r", encoding="utf-8") as arquivo:
        solicitacoes = json.load(arquivo)

# Se o arquivo ainda não existir, o programa começa com uma lista vazia.
except FileNotFoundError:
    solicitacoes = []


# Laço principal do sistema.
# Enquanto o usuário não escolher a opção 0, o menu continuará sendo exibido.
while True:

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

    # Recebe a opção escolhida pelo usuário.
    opcao = int(input("Escolha uma opção: "))
    print()


    # ==================================================
    # OPÇÃO 1 - CADASTRAR NOVA SOLICITAÇÃO
    # ==================================================

    if opcao == 1:

        print("========================================")
        print("          NOVA SOLICITAÇÃO              ")
        print("========================================")
        print()

        # Recebe o nome da pessoa que está fazendo a solicitação.
        solicitante = input("Informe o nome do solicitante: ")
        print()

        # O usuário escolhe para qual setor deseja enviar a solicitação.
        print("Selecione o setor responsável:")
        print()
        print("1 - Controladoria")
        print("2 - Recursos Humanos")
        print()

        setor = int(input("Escolha uma opção: "))
        print()


        # Se o setor escolhido for Controladoria.
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

            # Recebe o tipo de solicitação.
            tipo = int(input("Escolha o tipo de solicitação: "))

            # Converte a opção numérica em um texto.
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


        # Se o setor escolhido for Recursos Humanos.
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

            # Converte a opção numérica em um texto.
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


        # Caso o usuário escolha um setor que não existe.
        else:
            print("Setor inválido.")

            # O continue interrompe esta repetição do while
            # e volta imediatamente para o menu principal.
            continue


        # Recebe uma descrição mais detalhada da solicitação.
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


        # Cria um dicionário contendo os dados da solicitação.
        solicitacao = {

            # O ID é gerado de acordo com a quantidade atual de solicitações.
            "id": len(solicitacoes) + 1,

            "solicitante": solicitante,
            "setor": nome_setor,
            "tipo": tipo_solicitacao,
            "descricao": descricao,

            # Toda nova solicitação começa com o status "Aberta".
            "status": "Aberta"
        }


        # Adiciona o dicionário "solicitacao" dentro da lista "solicitacoes".
        solicitacoes.append(solicitacao)


        # Abre o arquivo JSON no modo de escrita.
        # O conteúdo da lista é salvo para não ser perdido ao fechar o programa.
        with open("solicitacoes.json", "w", encoding="utf-8") as arquivo:

            json.dump(
                solicitacoes,
                arquivo,
                ensure_ascii=False,
                indent=4
            )


        print("Solicitação cadastrada com sucesso!")
        print("Número da solicitação:", solicitacao["id"])


    # ==================================================
    # OPÇÃO 2 - LISTAR TODAS AS SOLICITAÇÕES
    # ==================================================

    elif opcao == 2:

        print("========================================")
        print("        LISTA DE SOLICITAÇÕES")
        print("========================================")
        print()

        # Verifica se a lista está vazia.
        if len(solicitacoes) == 0:
            print("Nenhuma solicitação cadastrada.")

        else:

            # Percorre todas as solicitações existentes na lista.
            for solicitacao in solicitacoes:

                print("ID............:", solicitacao["id"])
                print("Solicitante...:", solicitacao["solicitante"])
                print("Setor.........:", solicitacao["setor"])
                print("Tipo..........:", solicitacao["tipo"])
                print("Descrição.....:", solicitacao["descricao"])
                print("Status........:", solicitacao["status"])
                print("----------------------------------------")


    # ==================================================
    # OPÇÃO 3 - CONSULTAR UMA SOLICITAÇÃO PELO ID
    # ==================================================

    elif opcao == 3:

        print("========================================")
        print("       CONSULTAR SOLICITAÇÃO")
        print("========================================")
        print()

        # Recebe o ID que será procurado.
        id_busca = int(input("Informe o ID da solicitação: "))
        print()

        # Variável usada para saber se a solicitação foi encontrada.
        encontrada = False


        # Percorre toda a lista de solicitações.
        for solicitacao in solicitacoes:

            # Compara o ID atual com o ID informado pelo usuário.
            if solicitacao["id"] == id_busca:

                print("ID............:", solicitacao["id"])
                print("Solicitante...:", solicitacao["solicitante"])
                print("Setor.........:", solicitacao["setor"])
                print("Tipo..........:", solicitacao["tipo"])
                print("Descrição.....:", solicitacao["descricao"])
                print("Status........:", solicitacao["status"])

                # Marca que a solicitação foi encontrada.
                encontrada = True

                # Como o ID já foi encontrado, não é necessário continuar o for.
                break


        # Se o for terminar e "encontrada" continuar False,
        # significa que nenhum ID correspondente foi localizado.
        if encontrada == False:
            print("Solicitação não encontrada.")


    # ==================================================
    # OPÇÃO 4 - ALTERAR STATUS
    # ==================================================

    elif opcao == 4:

        print("========================================")
        print("          ALTERAR STATUS")
        print("========================================")
        print()

        id_busca = int(input("Informe o ID da solicitação: "))
        print()

        encontrada = False


        # Procura a solicitação pelo ID.
        for solicitacao in solicitacoes:

            if solicitacao["id"] == id_busca:

                encontrada = True

                print("Solicitação encontrada!")
                print()
                print("Status atual:", solicitacao["status"])
                print()

                print("1 - Aberta")
                print("2 - Em análise")
                print("3 - Aguardando informações")
                print("4 - Concluída")
                print("5 - Cancelada")
                print()

                novo_status = int(input("Escolha o novo status: "))
                print()


                # Altera somente o campo "status" do dicionário.
                if novo_status == 1:
                    solicitacao["status"] = "Aberta"

                elif novo_status == 2:
                    solicitacao["status"] = "Em análise"

                elif novo_status == 3:
                    solicitacao["status"] = "Aguardando informações"

                elif novo_status == 4:
                    solicitacao["status"] = "Concluída"

                elif novo_status == 5:
                    solicitacao["status"] = "Cancelada"

                else:
                    print("Status inválido.")
                    break


                # Salva a alteração realizada no arquivo JSON.
                with open("solicitacoes.json", "w", encoding="utf-8") as arquivo:

                    json.dump(
                        solicitacoes,
                        arquivo,
                        ensure_ascii=False,
                        indent=4
                    )


                print("Status alterado com sucesso!")
                print("Novo status:", solicitacao["status"])

                break


        if encontrada == False:
            print("Solicitação não encontrada.")


    # ==================================================
    # OPÇÃO 5 - FINALIZAR SOLICITAÇÃO
    # ==================================================

    elif opcao == 5:

        print("========================================")
        print("        FINALIZAR SOLICITAÇÃO")
        print("========================================")
        print()

        id_busca = int(input("Informe o ID da solicitação: "))
        print()

        encontrada = False


        # Percorre a lista procurando o ID informado.
        for solicitacao in solicitacoes:

            if solicitacao["id"] == id_busca:

                encontrada = True

                print("Solicitação encontrada!")
                print()
                print("Solicitante...:", solicitacao["solicitante"])
                print("Tipo..........:", solicitacao["tipo"])
                print("Status atual..:", solicitacao["status"])
                print()

                # Pede uma confirmação antes de finalizar.
                confirmacao = input(
                    "Deseja finalizar esta solicitação? (S/N): "
                )


                # Aceita tanto S maiúsculo quanto s minúsculo.
                if confirmacao == "S" or confirmacao == "s":

                    # Finalizar significa alterar o status para Concluída.
                    solicitacao["status"] = "Concluída"


                    # Salva a alteração no arquivo JSON.
                    with open(
                        "solicitacoes.json",
                        "w",
                        encoding="utf-8"
                    ) as arquivo:

                        json.dump(
                            solicitacoes,
                            arquivo,
                            ensure_ascii=False,
                            indent=4
                        )


                    print()
                    print("Solicitação finalizada com sucesso!")
                    print("Novo status:", solicitacao["status"])

                else:
                    print()
                    print("Finalização cancelada.")

                break


        if encontrada == False:
            print("Solicitação não encontrada.")


    # ==================================================
    # OPÇÃO 6 - RELATÓRIOS
    # ==================================================

    elif opcao == 6:

        print("========================================")
        print("              RELATÓRIOS")
        print("========================================")
        print()


        # Quantidade total de elementos da lista.
        total = len(solicitacoes)


        # Contadores de solicitações por setor.
        controladoria = 0
        rh = 0


        # Contadores de solicitações por status.
        abertas = 0
        em_analise = 0
        aguardando = 0
        concluidas = 0
        canceladas = 0


        # Percorre todas as solicitações para fazer as contagens.
        for solicitacao in solicitacoes:


            # Conta por setor.
            if solicitacao["setor"] == "Controladoria":
                controladoria += 1

            elif solicitacao["setor"] == "Recursos Humanos":
                rh += 1


            # Conta por status.
            if solicitacao["status"] == "Aberta":
                abertas += 1

            elif solicitacao["status"] == "Em análise":
                em_analise += 1

            elif solicitacao["status"] == "Aguardando informações":
                aguardando += 1

            elif solicitacao["status"] == "Concluída":
                concluidas += 1

            elif solicitacao["status"] == "Cancelada":
                canceladas += 1


        # Exibe o resultado das contagens.
        print("Total de solicitações........:", total)
        print()

        print("POR SETOR")
        print("Controladoria................:", controladoria)
        print("Recursos Humanos.............:", rh)
        print()

        print("POR STATUS")
        print("Abertas......................:", abertas)
        print("Em análise...................:", em_analise)
        print("Aguardando informações.......:", aguardando)
        print("Concluídas...................:", concluidas)
        print("Canceladas...................:", canceladas)


    # ==================================================
    # OPÇÃO 0 - ENCERRAR O SISTEMA
    # ==================================================

    elif opcao == 0:

        print("Encerrando o sistema...")

        # Interrompe o while True e encerra o programa.
        break


    # Caso o usuário informe uma opção que não existe no menu.
    else:
        print("Opção inválida.")


    # Cria uma linha em branco antes de mostrar o menu novamente.
    print()