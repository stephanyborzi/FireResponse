# Simulador de Resposta a Queimadas

## Descrição

Este projeto é um simulador de resposta a queimadas florestais que utiliza dados reais da NASA para detectar ocorrências de incêndios. Ele prioriza as ocorrências de acordo com sua severidade calculada, usando programação dinâmica para otimizar o cálculo da severidade com memorização.

## Funcionalidades

- Integração com API da NASA para obter dados de queimadas em tempo real.
- Cálculo de severidade da ocorrência usando parâmetros como brilho, FRP e confiabilidade.
- Prioridade no atendimento das ocorrências baseada em uma fila de prioridade (heap).
- Métodos para inserir ocorrência, atender próximas ocorrências de forma recursiva.
- Histórico de atendimentos e relatório por região.
- Uso de programação dinâmica (memorização) para otimizar o cálculo da severidade.

## Conceitos Aplicados

- **Programação Dinâmica:** Memorização para evitar cálculos repetidos.
- **Heap (Fila de Prioridade):** Para gerenciamento eficiente das ocorrências.
- **Recursão:** Para atender múltiplas ocorrências.
- **Tratamento de dados reais:** Consumo e parsing de dados CSV da NASA.

## Requisitos

- Python 3.7+
- Biblioteca `requests`

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL-do-repositorio>
   cd <nome-do-projeto>
