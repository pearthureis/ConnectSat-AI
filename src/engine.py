import requests


def analisar_missao(dados, alertas):
    prompt = f"""
Você é um engenheiro especialista no satélite ConnectSat.

Analise estes dados:

- Latência: {dados['latencia_ms']} ms
- Throughput: {dados['throughput_mbps']} Mbps
- Temperatura: {dados['temperatura_transponder']} °C
- Qualidade do sinal: {dados['qualidade_sinal']}%

Alertas:
{chr(10).join(alertas) if alertas else "Nenhum"}

Explique:
1. O estado geral da missão.
2. Os problemas encontrados.
3. O impacto para escolas rurais, postos de saúde e comunidades isoladas.
4. As ações recomendadas.
"""

    try:
        resposta = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        resposta.raise_for_status()
        return resposta.json().get("response", "Nenhuma resposta recebida da IA.")

    except Exception as e:
        return f"Erro ao consultar o Ollama: {e}"