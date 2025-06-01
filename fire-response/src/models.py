import heapq

class Ocorrencia:
    def __init__(self, id, latitude, longitude, severidade, data):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.severidade = severidade
        self.data = data
        self.status = "pendente"

    def __lt__(self, other):
        return self.severidade > other.severidade

class EquipeResposta:
    def __init__(self):
        self.ocorrencias = []
        self.historico = []

    def inserir_ocorrencia(self, ocorrencia):
        heapq.heappush(self.ocorrencias, ocorrencia)

    def atender_proxima(self):
        if self.ocorrencias:
            ocorrencia = heapq.heappop(self.ocorrencias)
            ocorrencia.status = "atendida"
            self.historico.append(ocorrencia)
            print(f"[✔] Ocorrência atendida: {ocorrencia.id} | Severidade: {ocorrencia.severidade}")
        else:
            print("[!] Nenhuma ocorrência pendente.")

    def atender_proximas_recursivamente(self, n):
        if n == 0 or not self.ocorrencias:
            return
        self.atender_proxima()
        self.atender_proximas_recursivamente(n - 1)

    def listar_historico(self):
        print("\n[Histórico de Atendimentos]")
        for o in self.historico:
            print(f"ID: {o.id}, Severidade: {o.severidade}, Data: {o.data}, Status: {o.status}")

    def gerar_relatorio_regiao(self):
        relatorio = {}
        for o in self.historico:
            regiao = f"({round(o.latitude, 1)},{round(o.longitude, 1)})"
            relatorio[regiao] = relatorio.get(regiao, 0) + 1
        print("\n[Relatório por Região]")
        for regiao, atendidas in relatorio.items():
            print(f"Região {regiao}: {atendidas} atendimentos")
