import requests
from datetime import datetime

def carregar_dados_nasa(api_key):
    hoje = datetime.today().strftime('%Y-%m-%d')
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{api_key}/MODIS_NRT/world/10/{hoje}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.text.splitlines()
        return dados[1:21]  
    else:
        print(f"Erro ao acessar NASA: {resposta.status_code}")
        return []
