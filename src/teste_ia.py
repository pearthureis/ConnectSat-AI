import requests

resposta = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": "Diga apenas: Olá!",
        "stream": False
    }
)

print(resposta.status_code)
print(resposta.text)