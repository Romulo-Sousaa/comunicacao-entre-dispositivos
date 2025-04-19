import numpy as np
import matplotlib.pyplot as plt
from datagramas import dados
from enquadramento import armazenar_dados

dados_originais = dados()
dados, indice = armazenar_dados(dados_originais)

# Parâmetros do sinal
amplitude_1 = 1.0   # para bit 1
amplitude_0 = 0.0   # para bit 0
bit_duration = 1    # duração de cada bit em segundos
sampling_rate = 100  # amostras por segundo
samples_per_bit = int(sampling_rate * bit_duration)
N = 20  # número de bits a exibir (evita gráfico enorme)

plt.figure(figsize=(14, 12))

for idx, quadro in enumerate(dados):
    quadro = quadro[:N]  # limitar número de bits

    ## --- ASK ---
    t = np.linspace(0, len(quadro) * bit_duration, len(quadro) * samples_per_bit)
    sinal_ask = np.zeros_like(t)

    for i, bit in enumerate(quadro):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        amplitude = amplitude_1 if bit == '1' else amplitude_0
        sinal_ask[start:end] = amplitude

    plt.subplot(6, 1, idx * 2 + 1)  # posições: 1, 3, 5
    plt.plot(t, sinal_ask, label='ASK', color='blue')
    plt.title(f'Modulação ASK - Quadro {indice + 1} do Datagrama {idx + 1}')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.ylim(-0.2, 1.2)
    plt.grid(True)

    ## --- FSK ---
    f_0 = 5
    f_1 = 10
    sinal_fsk = np.zeros_like(t)

    for i, bit in enumerate(quadro):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        t_bit = np.linspace(0, bit_duration, samples_per_bit, endpoint=False)
        freq = f_1 if bit == '1' else f_0
        sinal_fsk[start:end] = np.sin(2 * np.pi * freq * t_bit)

    plt.subplot(6, 1, idx * 2 + 2)  # posições: 2, 4, 6
    plt.plot(t, sinal_fsk, label='FSK', color='green')
    plt.title(f'Modulação FSK - Quadro {indice + 1} do Datagrama {idx + 1}')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)

plt.tight_layout()
plt.show()
