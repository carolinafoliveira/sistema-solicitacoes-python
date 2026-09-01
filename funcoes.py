import json
from datetime import datetime


# ==================================================
# FUNÇÃO PARA LER NÚMEROS INTEIROS
# ==================================================

def ler_inteiro(mensagem):
    """
    Tenta converter a entrada do usuário para inteiro.

    Se o usuário digitar texto ou um valor inválido,
    o programa informa o erro e pede novamente.
    """

    while True:

        try:
            numero = int(input(mensagem))
            return numero

        except ValueError:
            print("Digite apenas números.")
            print()


# ==================================================
# FUNÇÃO PARA LER OPÇÕES VÁLIDAS
# ==================================================

def ler_opcao(mensagem, minimo, maximo):
    """
    Lê uma opção numérica e verifica se ela está
    dentro do intervalo permitido.
    """

    while True:

        opcao = ler_inteiro(mensagem)

        if opcao >= minimo and opcao <= maximo:
            return opcao

        print("Opção inválida.")
        print()


# ==================================================
# FUNÇÃO PARA CARREGAR SOLICITAÇÕES
# ==================================================

def carregar_solicitacoes():
    """
    Carrega as solicitações existentes no arquivo JSON.

    Se o arquivo não existir, retorna uma lista vazia.
    """

    try:

        with open(
            "solicitacoes.json",
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    except FileNotFoundError:

        return []


# ==================================================
# FUNÇÃO PARA SALVAR SOLICITAÇÕES
# ==================================================

def salvar_solicitacoes(solicitacoes):
    """
    Salva a lista de solicitações no arquivo JSON.
    """

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


# ==================================================
# FUNÇÃO PARA GERAR NOVO ID
# ==================================================

def gerar_id(solicitacoes):
    """
    Gera um novo ID.

    O novo ID será sempre o maior ID existente + 1.
    """

    if len(solicitacoes) == 0:

        return 1

    maior_id = 0

    for solicitacao in solicitacoes:

        if solicitacao["id"] > maior_id:

            maior_id = solicitacao["id"]

    return maior_id + 1


# ==================================================
# FUNÇÃO PARA CADASTRAR NOVA SOLICITAÇÃO
# ==================================================

def nova_solicitacao(solicitacoes):

    print("========================================")
    print("          NOVA SOLICITAÇÃO")
    print("========================================")
    print()

    solicitante = input(
        "Informe o nome do solicitante: "
    )

    print()

    print("Selecione o setor responsável:")
    print()
    print("1 - Controladoria")
    print("2 - Recursos Humanos")
    print()

    setor = ler_opcao(
        "Escolha uma opção: ",
        1,
        2
    )

    print()


    # ----------------------------------------------
    # CONTROLADORIA
    # ----------------------------------------------

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

        tipo = ler_opcao(
            "Escolha o tipo de solicitação: ",
            1,
            5
        )

        if tipo == 1:

            tipo_solicitacao = (
                "Comprovante de pagamento"
            )

        elif tipo == 2:

            tipo_solicitacao = (
                "Confirmação de recebimento de cliente"
            )

        elif tipo == 3:

            tipo_solicitacao = (
                "Relatório para diretoria/gerência"
            )

        elif tipo == 4:

            tipo_solicitacao = "Dados cadastrais"

        elif tipo == 5:

            tipo_solicitacao = "Outros"


    # ----------------------------------------------
    # RECURSOS HUMANOS
    # ----------------------------------------------

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

        tipo = ler_opcao(
            "Escolha o tipo de solicitação: ",
            1,
            5
        )

        if tipo == 1:

            tipo_solicitacao = "Holerite"

        elif tipo == 2:

            tipo_solicitacao = (
                "Informe de rendimentos"
            )

        elif tipo == 3:

            tipo_solicitacao = (
                "Documentos de plano de saúde"
            )

        elif tipo == 4:

            tipo_solicitacao = (
                "Calendário de exames médicos periódicos"
            )

        elif tipo == 5:

            tipo_solicitacao = "Outros"


    # ----------------------------------------------
    # DESCRIÇÃO
    # ----------------------------------------------

    print()

    descricao = input(
        "Descreva a solicitação: "
    )

    print()


    # ----------------------------------------------
    # GERAÇÃO DO ID
    # ----------------------------------------------

    novo_id = gerar_id(solicitacoes)


    # ----------------------------------------------
    # DATA DE ABERTURA
    # ----------------------------------------------

    data_abertura = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )


    # ----------------------------------------------
    # CRIAÇÃO DA SOLICITAÇÃO
    # ----------------------------------------------

    solicitacao = {

        "id": novo_id,

        "solicitante": solicitante,

        "setor": nome_setor,

        "tipo": tipo_solicitacao,

        "descricao": descricao,

        "status": "Aberta",

        "data_abertura": data_abertura,

        "data_finalizacao": None
    }


    # Adiciona a solicitação à lista.
    solicitacoes.append(solicitacao)


    # Salva os dados no JSON.
    salvar_solicitacoes(solicitacoes)


    # ----------------------------------------------
    # RESUMO
    # ----------------------------------------------

    print("========================================")
    print("        RESUMO DA SOLICITAÇÃO")
    print("========================================")
    print()

    print(
        "ID............:",
        solicitacao["id"]
    )

    print(
        "Solicitante...:",
        solicitacao["solicitante"]
    )

    print(
        "Setor.........:",
        solicitacao["setor"]
    )

    print(
        "Tipo..........:",
        solicitacao["tipo"]
    )

    print(
        "Descrição.....:",
        solicitacao["descricao"]
    )

    print(
        "Status........:",
        solicitacao["status"]
    )

    print(
        "Abertura......:",
        solicitacao["data_abertura"]
    )

    print()

    print(
        "Solicitação cadastrada com sucesso!"
    )


# ==================================================
# FUNÇÃO PARA LISTAR SOLICITAÇÕES
# ==================================================

def listar_solicitacoes(solicitacoes):

    print("========================================")
    print("        LISTA DE SOLICITAÇÕES")
    print("========================================")
    print()

    if len(solicitacoes) == 0:

        print(
            "Nenhuma solicitação cadastrada."
        )

        return


    for solicitacao in solicitacoes:

        print(
            "ID............:",
            solicitacao["id"]
        )

        print(
            "Solicitante...:",
            solicitacao["solicitante"]
        )

        print(
            "Setor.........:",
            solicitacao["setor"]
        )

        print(
            "Tipo..........:",
            solicitacao["tipo"]
        )

        print(
            "Descrição.....:",
            solicitacao["descricao"]
        )

        print(
            "Status........:",
            solicitacao["status"]
        )

        print(
            "Abertura......:",
            solicitacao.get(
                "data_abertura",
                "Não registrada"
            )
        )

        print(
            "Finalização...:",
            solicitacao.get(
                "data_finalizacao"
            ) or "Não finalizada"
        )

        print(
            "----------------------------------------"
        )


# ==================================================
# FUNÇÃO PARA CONSULTAR SOLICITAÇÃO
# ==================================================

def consultar_solicitacao(solicitacoes):

    print("========================================")
    print("       CONSULTAR SOLICITAÇÃO")
    print("========================================")
    print()

    id_busca = ler_inteiro(
        "Informe o ID da solicitação: "
    )

    print()

    encontrada = False


    for solicitacao in solicitacoes:

        if solicitacao["id"] == id_busca:

            print(
                "ID............:",
                solicitacao["id"]
            )

            print(
                "Solicitante...:",
                solicitacao["solicitante"]
            )

            print(
                "Setor.........:",
                solicitacao["setor"]
            )

            print(
                "Tipo..........:",
                solicitacao["tipo"]
            )

            print(
                "Descrição.....:",
                solicitacao["descricao"]
            )

            print(
                "Status........:",
                solicitacao["status"]
            )

            print(
                "Abertura......:",
                solicitacao.get(
                    "data_abertura",
                    "Não registrada"
                )
            )

            print(
                "Finalização...:",
                solicitacao.get(
                    "data_finalizacao"
                ) or "Não finalizada"
            )

            encontrada = True

            break


    if encontrada == False:

        print(
            "Solicitação não encontrada."
        )


# ==================================================
# FUNÇÃO PARA ALTERAR STATUS
# ==================================================

def alterar_status(solicitacoes):

    print("========================================")
    print("          ALTERAR STATUS")
    print("========================================")
    print()

    id_busca = ler_inteiro(
        "Informe o ID da solicitação: "
    )

    print()

    encontrada = False


    for solicitacao in solicitacoes:

        if solicitacao["id"] == id_busca:

            encontrada = True

            print(
                "Solicitação encontrada!"
            )

            print()

            print(
                "Status atual:",
                solicitacao["status"]
            )

            print()

            print("1 - Aberta")
            print("2 - Em análise")
            print("3 - Aguardando informações")
            print("4 - Concluída")
            print("5 - Cancelada")
            print()

            novo_status = ler_opcao(
                "Escolha o novo status: ",
                1,
                5
            )

            print()


            if novo_status == 1:

                solicitacao["status"] = "Aberta"

            elif novo_status == 2:

                solicitacao["status"] = (
                    "Em análise"
                )

            elif novo_status == 3:

                solicitacao["status"] = (
                    "Aguardando informações"
                )

            elif novo_status == 4:

                solicitacao["status"] = (
                    "Concluída"
                )

                solicitacao[
                    "data_finalizacao"
                ] = datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

            elif novo_status == 5:

                solicitacao["status"] = (
                    "Cancelada"
                )


            # Se o status deixou de ser concluído,
            # remove a data de finalização.
            if novo_status != 4:

                solicitacao[
                    "data_finalizacao"
                ] = None


            salvar_solicitacoes(
                solicitacoes
            )

            print(
                "Status alterado com sucesso!"
            )

            print(
                "Novo status:",
                solicitacao["status"]
            )

            break


    if encontrada == False:

        print(
            "Solicitação não encontrada."
        )


# ==================================================
# FUNÇÃO PARA FINALIZAR SOLICITAÇÃO
# ==================================================

def finalizar_solicitacao(solicitacoes):

    print("========================================")
    print("        FINALIZAR SOLICITAÇÃO")
    print("========================================")
    print()

    id_busca = ler_inteiro(
        "Informe o ID da solicitação: "
    )

    print()

    encontrada = False


    for solicitacao in solicitacoes:

        if solicitacao["id"] == id_busca:

            encontrada = True

            print(
                "Solicitação encontrada!"
            )

            print()

            print(
                "Solicitante...:",
                solicitacao["solicitante"]
            )

            print(
                "Tipo..........:",
                solicitacao["tipo"]
            )

            print(
                "Status atual..:",
                solicitacao["status"]
            )

            print()

            confirmacao = input(
                "Deseja finalizar esta solicitação? (S/N): "
            )


            if confirmacao.lower() == "s":

                solicitacao["status"] = (
                    "Concluída"
                )

                solicitacao[
                    "data_finalizacao"
                ] = datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )

                salvar_solicitacoes(
                    solicitacoes
                )

                print()

                print(
                    "Solicitação finalizada com sucesso!"
                )

                print(
                    "Novo status:",
                    solicitacao["status"]
                )

                print(
                    "Data da finalização:",
                    solicitacao[
                        "data_finalizacao"
                    ]
                )

            else:

                print()

                print(
                    "Finalização cancelada."
                )

            break


    if encontrada == False:

        print(
            "Solicitação não encontrada."
        )


# ==================================================
# FUNÇÃO PARA RELATÓRIOS
# ==================================================

def relatorios(solicitacoes):

    print("========================================")
    print("              RELATÓRIOS")
    print("========================================")
    print()

    total = len(solicitacoes)

    controladoria = 0
    rh = 0

    abertas = 0
    em_analise = 0
    aguardando = 0
    concluidas = 0
    canceladas = 0


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

        elif solicitacao["status"] == (
            "Aguardando informações"
        ):

            aguardando += 1

        elif solicitacao["status"] == "Concluída":

            concluidas += 1

        elif solicitacao["status"] == "Cancelada":

            canceladas += 1


    print(
        "Total de solicitações........:",
        total
    )

    print()

    print("POR SETOR")

    print(
        "Controladoria................:",
        controladoria
    )

    print(
        "Recursos Humanos.............:",
        rh
    )

    print()

    print("POR STATUS")

    print(
        "Abertas......................:",
        abertas
    )

    print(
        "Em análise...................:",
        em_analise
    )

    print(
        "Aguardando informações.......:",
        aguardando
    )

    print(
        "Concluídas...................:",
        concluidas
    )

    print(
        "Canceladas...................:",
        canceladas
    )


# ==================================================
# FUNÇÃO PARA EXIBIR MENU
# ==================================================

def exibir_menu():

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
