# Lista para armazenar as informações de eventos
historico_acoes = []

def registrar_acao(acao):
    """Adiciona uma ação ao histórico do jogo."""
    historico_acoes.append(acao)

def exibir_historico():
    """Imprime o registro completo ao final da partida."""
    print("\n" + "="*30)
    print("📜 HISTÓRICO DA PARTIDA 📜")
    print("="*30)
    for i, acao in enumerate(historico_acoes, start=1):
        print(f"{i}. {acao}")
    print("="*30 + "\n")