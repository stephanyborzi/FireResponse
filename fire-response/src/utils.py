import random

severidade_cache = {}

def calcular_severidade_memo(brilho, frp, confianca):
    chave = (brilho, frp, confianca)
    if chave in severidade_cache:
        return severidade_cache[chave]
    severidade = round((brilho * 0.4) + (frp * 0.3) + (confianca * 0.3), 2)
    severidade_cache[chave] = severidade
    return severidade

from models import Ocorrencia

def simular_ocorrencias(equipe, dados_csv):
    for linha in dados_csv:
        partes = linha.split(",")
        try:
            lat = float(partes[0])
            long = float(partes[1])
            bright = float(partes[2])
            frp = float(partes[11])
            confid_raw = partes[8]
            date = partes[5]

            if confid_raw.isdigit():
                confid = int(confid_raw)
            elif confid_raw.lower() == "low":
                confid = 30
            elif confid_raw.lower() == "nominal":
                confid = 60
            elif confid_raw.lower() == "high":
                confid = 90
            else:
                confid = 50

            id = random.randint(1000, 9999)
            severidade = calcular_severidade_memo(bright, frp, confid)
            ocorrencia = Ocorrencia(id, lat, long, severidade, date)
            equipe.inserir_ocorrencia(ocorrencia)
        except Exception as e:
            print(f"[!] Erro ao processar linha: {linha}\n{e}")
