def analisar_missao(dados, alertas):
    if not alertas:
        return (
            "A missão está operando normalmente. "
            "O satélite mantém conectividade estável para escolas, "
            "postos de saúde e comunidades rurais."
        )

    resposta = "Foram detectados os seguintes problemas:\n"

    for alerta in alertas:
        resposta += f"- {alerta}\n"

    resposta += (
        "\nEssas falhas podem causar lentidão ou interrupção do serviço "
        "de internet, afetando aulas online, telemedicina e a comunicação "
        "de comunidades que dependem do ConnectSat."
    )

    return resposta