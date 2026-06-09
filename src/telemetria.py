import random

def gerar_telemetria():
    return {
        "latencia_ms": random.randint(100, 1000),
        "throughput_mbps": random.randint(20, 300),
        "temperatura_transponder": random.randint(20, 90),
        "qualidade_sinal": random.randint(30, 100)
    }