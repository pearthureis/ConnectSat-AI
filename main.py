from src.telemetria import gerar_telemetria
from src.alertas import verificar_alertas
from src.engine import analisar_missao
from src.ui import exibir_cabecalho

while True:
    exibir_cabecalho()

    print("1 - Gerar telemetria")
    print("2 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        dados = gerar_telemetria()
        alertas = verificar_alertas(dados)

        print("\n=== TELEMETRIA ===")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

        print("\n=== ALERTAS ===")
        if alertas:
            for alerta in alertas:
                print(alerta)
        else:
            print("Nenhum alerta encontrado.")

        print("\n🤖 Gerando análise da IA... Aguarde alguns segundos.")

        analise = analisar_missao(dados, alertas)

        print("\n===== ANÁLISE DA IA =====")
        print(analise)

        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "2":
        print("Encerrando o ConnectSat AI...")
        break

    else:
        print("Opção inválida.")
        input("\nPressione Enter para continuar...")