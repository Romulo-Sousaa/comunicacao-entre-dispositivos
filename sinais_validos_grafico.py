import matplotlib.pyplot as plt

def plotar_3_quadros_em_linhas(dados_binarios):
    """
    Plota até 3 sinais digitais (quadros) em 3 linhas diferentes no mesmo gráfico.
    """
    num_quadros = min(3, len(dados_binarios))
    plt.figure(figsize=(12, 6))

    for idx in range(num_quadros):
        quadro = dados_binarios[idx]
        bits = list(map(int, quadro))
        tempo = list(range(len(bits)))

        plt.subplot(3, 1, idx + 1)
        plt.step(tempo, bits, where='post', label=f'Quadro {idx + 1}')
        plt.title(f'Sinal Digital - Quadro {idx + 1}')
        plt.ylim(-0.2, 1.2)
        plt.xlabel("Tempo (bits)")
        plt.ylabel("Nível")
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.show()

