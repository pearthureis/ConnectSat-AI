def verificar_alertas(dados):
    alertas = []

    if dados["latencia_ms"] > 700:
        alertas.append("Latência muito alta.")

    if dados["throughput_mbps"] < 50:
        alertas.append("Velocidade de transmissão muito baixa.")

    if dados["temperatura_transponder"] > 75:
        alertas.append("Transponder superaquecido.")

    if dados["qualidade_sinal"] < 50:
        alertas.append("Qualidade do sinal muito baixa.")

    return alertas