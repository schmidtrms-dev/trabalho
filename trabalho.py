# Sistema de Automacao Digital: Gestao de Pecas, Qualidade e Armazenamento

pecas_cadastradas = []
CAPACIDADE_CAIXA = 10


def avaliar_peca(peso, cor, comprimento):
    motivos_reprovacao = []

    if not (95 <= peso <= 105):
        motivos_reprovacao.append(f"Peso fora do padrao ({peso}g - exigido entre 95g e 105g)")

    if cor.lower() not in ["azul", "verde"]:
        motivos_reprovacao.append(f"Cor invalida ('{cor}' - exigido azul ou verde)")

    if not (10 <= comprimento <= 20):
        motivos_reprovacao.append(
            f"Comprimento fora do padrao ({comprimento}cm - exigido entre 10cm e 20cm)"
        )

    aprovada = len(motivos_reprovacao) == 0
    return aprovada, motivos_reprovacao


def obter_pecas_aprovadas():
    return [p for p in pecas_cadastradas if p["aprovada"]]


def obter_pecas_reprovadas():
    return [p for p in pecas_cadastradas if not p["aprovada"]]


def organizar_caixas():
    aprovadas = obter_pecas_aprovadas()
    caixas_fechadas = []
    caixa_atual = []

    for peca in aprovadas:
        caixa_atual.append(peca)
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []

    return caixas_fechadas, caixa_atual


def cadastrar_peca():
    print("\n--- CADASTRAR NOVA PECA ---")
    id_peca = input("Digite o ID da peca: ").strip()

    if not id_peca:
        print("Erro: O ID da peca nao pode ser vazio.")
        return

    for p in pecas_cadastradas:
        if p["id"].lower() == id_peca.lower():
            print(f"Erro: Ja existe uma peca cadastrada com o ID '{id_peca}'.")
            return

    try:
        peso = float(input("Digite o peso da peca (em gramas, ex: 100): ").replace(",", "."))
        cor = input("Digite a cor da peca (azul ou verde): ").strip().lower()
        comprimento = float(
            input("Digite o comprimento da peca (em cm, ex: 15): ").replace(",", ".")
        )
    except ValueError:
        print("Erro: Peso e comprimento devem ser valores numericos validos.")
        return

    aprovada, motivos = avaliar_peca(peso, cor, comprimento)

    nova_peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "aprovada": aprovada,
        "motivos": motivos,
    }

    pecas_cadastradas.append(nova_peca)

    if aprovada:
        print(f"\nResultado: Peca '{id_peca}' APROVADA.")
        caixas_fechadas, caixa_atual = organizar_caixas()
        if len(caixa_atual) == 0 and len(caixas_fechadas) > 0:
            print(
                f"Aviso de Armazenamento: A Caixa {len(caixas_fechadas)} atingiu a capacidade maxima de {CAPACIDADE_CAIXA} pecas e foi FECHADA."
            )
            print("Uma nova caixa foi iniciada para as proximas pecas.")
        else:
            numero_caixa_atual = len(caixas_fechadas) + 1
            print(
                f"Armazenamento: Peca alocada na Caixa {numero_caixa_atual} ({len(caixa_atual)}/{CAPACIDADE_CAIXA} pecas)."
            )
    else:
        print(f"\nResultado: Peca '{id_peca}' REPROVADA.")
        print("Motivo(s) da reprovacao:")
        for motivo in motivos:
            print(f" - {motivo}")


def listar_pecas():
    print("\n--- LISTA DE PECAS APROVADAS E REPROVADAS ---")
    if not pecas_cadastradas:
        print("Nenhuma peca cadastrada ate o momento.")
        return

    aprovadas = obter_pecas_aprovadas()
    reprovadas = obter_pecas_reprovadas()

    print(f"\nPECAS APROVADAS ({len(aprovadas)}):")
    if not aprovadas:
        print(" Nenhuma peca aprovada.")
    else:
        for p in aprovadas:
            print(
                f" - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm"
            )

    print(f"\nPECAS REPROVADAS ({len(reprovadas)}):")
    if not reprovadas:
        print(" Nenhuma peca reprovada.")
    else:
        for p in reprovadas:
            motivos_str = "; ".join(p["motivos"])
            print(
                f" - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm | Motivo(s): {motivos_str}"
            )


def remover_peca():
    print("\n--- REMOVER PECA CADASTRADA ---")
    if not pecas_cadastradas:
        print("Nenhuma peca cadastrada para remover.")
        return

    id_remover = input("Digite o ID da peca que deseja remover: ").strip()

    for i, p in enumerate(pecas_cadastradas):
        if p["id"].lower() == id_remover.lower():
            peca_removida = pecas_cadastradas.pop(i)
            status = "APROVADA" if peca_removida["aprovada"] else "REPROVADA"
            print(f"Peca ID '{peca_removida['id']}' (Status: {status}) foi removida com sucesso.")
            return

    print(f"Peca com ID '{id_remover}' nao encontrada.")


def listar_caixas_fechadas():
    print("\n--- LISTA DE CAIXAS FECHADAS ---")
    caixas_fechadas, caixa_atual = organizar_caixas()

    if not caixas_fechadas:
        print("Nenhuma caixa fechada ate o momento (necessario 10 pecas aprovadas por caixa).")
    else:
        for indice, caixa in enumerate(caixas_fechadas, start=1):
            ids_pecas = ", ".join([p["id"] for p in caixa])
            print(f"Caixa {indice} [FECHADA - {len(caixa)}/{CAPACIDADE_CAIXA} pecas]: IDs ({ids_pecas})")

    if caixa_atual:
        ids_atuais = ", ".join([p["id"] for p in caixa_atual])
        print(
            f"\nCaixa {len(caixas_fechadas) + 1} [EM ABERTO - {len(caixa_atual)}/{CAPACIDADE_CAIXA} pecas]: IDs ({ids_atuais})"
        )


def gerar_relatorio_final():
    print("\n==================================================")
    print("        RELATORIO CONSOLIDADO DE PRODUCAO         ")
    print("==================================================")

    aprovadas = obter_pecas_aprovadas()
    reprovadas = obter_pecas_reprovadas()
    caixas_fechadas, caixa_atual = organizar_caixas()

    total_caixas_utilizadas = len(caixas_fechadas) + (1 if len(caixa_atual) > 0 else 0)

    print(f"Total de pecas produzidas/analisadas : {len(pecas_cadastradas)}")
    print(f"Total de pecas APROVADAS             : {len(aprovadas)}")
    print(f"Total de pecas REPROVADAS            : {len(reprovadas)}")
    print(f"Quantidade de caixas utilizadas      : {total_caixas_utilizadas}")
    print(f" - Caixas fechadas (10/10 pecas)     : {len(caixas_fechadas)}")
    if caixa_atual:
        print(f" - Caixa em aberto ({len(caixa_atual)}/10 pecas)      : 1")
    else:
        print(" - Caixa em aberto                   : 0")

    print("\nDETALHAMENTO DE REPROVACOES:")
    if not reprovadas:
        print(" Nenhuma peca foi reprovada.")
    else:
        for p in reprovadas:
            print(f" - Peca ID '{p['id']}':")
            for motivo in p["motivos"]:
                print(f"    * {motivo}")
    print("==================================================")


def exibir_menu():
    print("\n==================================================")
    print(" SISTEMA DE GESTAO DE PECAS, QUALIDADE E ESTOQUE ")
    print("==================================================")
    print("1. Cadastrar nova peca")
    print("2. Listar pecas aprovadas/reprovadas")
    print("3. Remover peca cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatorio final")
    print("0. Sair do sistema")
    print("==================================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio_final()
        elif opcao == "0":
            print("\nEncerrando o sistema. Ate logo!")
            break
        else:
            print("\nOpcao invalida. Por favor, escolha uma opcao de 0 a 5.")


if __name__ == "__main__":
    main()