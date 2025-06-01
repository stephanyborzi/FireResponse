from nasa_api import carregar_dados_nasa
from models import EquipeResposta
from utils import simular_ocorrencias

def main():
    api_key = "0805d1ba024fac58a269b2d8fd07483c"
    dados_csv = carregar_dados_nasa(api_key)

    if not dados_csv:
        print("[!] Nenhum dado carregado.")
        return

    equipe = EquipeResposta()
    simular_ocorrencias(equipe, dados_csv)
    equipe.atender_proximas_recursivamente(5)
    equipe.listar_historico()
    equipe.gerar_relatorio_regiao()

if __name__ == "__main__":
    main()
