import numpy as np
import matplotlib.pyplot as plt
from datagramas import dados
from enquadramento import armazenar_dados

dados_originais = dados()
dados, indice = armazenar_dados(dados_originais)

# Parâmetros da FSK
f_0 = 5   # frequência para bit 0 (Hz)
f_1 = 10  # frequência para bit 1 (Hz)
bit_duration = 1  # duração de cada bit (em segundos)
sampling_rate = 100  # amostras por segundo
samples_per_bit = int(sampling_rate * bit_duration)
N = 20

plt.figure(figsize=(36, 8))

for idx, quadro in enumerate(dados):
    quadro = quadro[:N]
    t_total = np.linspace(0, len(quadro) * bit_duration, len(quadro) * samples_per_bit)
    sinal = np.zeros_like(t_total)

    for i, bit in enumerate(quadro):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        t_bit = np.linspace(0, bit_duration, samples_per_bit, endpoint=False)

        if bit == '1':
            sinal[start:end] = np.sin(2 * np.pi * f_1 * t_bit)
        else:
            sinal[start:end] = np.sin(2 * np.pi * f_0 * t_bit)

    plt.subplot(3, 1, idx + 1)
    plt.plot(t_total, sinal, color='blue')
    plt.title(f'Modulação FSK do Quadro {indice + 1} do Datagrama {idx + 1}')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
plt.tight_layout()
plt.show()