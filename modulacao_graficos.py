import matplotlib.pyplot as plt

def grafico_modulacao(sinal_ask, sinal_fsk, tempo):
    plt.figure(figsize=(16, 6))

    # Gráfico ASK
    plt.subplot(2, 1, 1)
    plt.plot(tempo, sinal_ask, color='blue')
    plt.title('Modulação ASK - Sinal Multiplexado')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.ylim(-0.2, 1.2)
    plt.grid(True)

    # Gráfico FSK
    plt.subplot(2, 1, 2)
    plt.plot(tempo, sinal_fsk, color='green')
    plt.title('Modulação FSK - Sinal Multiplexado')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
