from src.telemetria import gerar_telemetria
from src.alertas import verificar_alertas

dados = gerar_telemetria()

print("===== CONNECTSAT AI =====")
print("Status atual do satélite:\n")

print(f"Latência: {dados['latencia_ms']} ms")
print(f"Throughput: {dados['throughput_mbps']} Mbps")
print(f"Temperatura: {dados['temperatura_transponder']} °C")
print(f"Qualidade do sinal: {dados['qualidade_sinal']} %")

print("\n===== ALERTAS =====")

alertas = verificar_alertas(dados)

if alertas:
    for alerta in alertas:
        print(alerta)
else:
    print("Nenhum problema detectado.")

from src.engine import analisar_missao

print("\n===== ANÁLISE DA IA =====")
print(analisar_missao(dados, alertas))