from funcoes import *

# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

solicitacoes = carregar_solicitacoes()


while True:

    exibir_menu()

    opcao = ler_opcao(
        "Escolha uma opção: ",
        0,
        6
    )

    print()


    if opcao == 1:

        nova_solicitacao(
            solicitacoes
        )


    elif opcao == 2:

        listar_solicitacoes(
            solicitacoes
        )


    elif opcao == 3:

        consultar_solicitacao(
            solicitacoes
        )


    elif opcao == 4:

        alterar_status(
            solicitacoes
        )


    elif opcao == 5:

        finalizar_solicitacao(
            solicitacoes
        )


    elif opcao == 6:

        relatorios(
            solicitacoes
        )


    elif opcao == 0:

        print(
            "Encerrando o sistema..."
        )

        break


    print()