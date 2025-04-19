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
samples_per_bit = 100  # resolução do sinal

plt.figure(figsize=(12, 8))

for idx, quadro in enumerate(dados):
    t = np.linspace(0, len(quadro)*bit_duration, len(quadro)*samples_per_bit)
    sinal = np.zeros_like(t)

    for i, bit in enumerate(quadro):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        amplitude = amplitude_1 if bit == '1' else amplitude_0
        sinal[start:end] = amplitude

    plt.subplot(3, 1, idx + 1)
    plt.plot(t, sinal, label='Sinal ASK', color='blue')
    plt.title(f'Modulação ASK do Quadro {indice + 1} do Datagrama {idx + 1}')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.ylim(-0.2, 1.2)
    plt.grid(True)

plt.tight_layout()
plt.show()