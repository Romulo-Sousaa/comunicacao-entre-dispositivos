import numpy as np
import matplotlib.pyplot as plt
from datagramas import dados
from enquadramento import armazenar_dados

dados_originais = dados()
dados, indice = armazenar_dados(dados_originais)

def gerar_sinal_tdm(datar):

    q1, q2, q3 = datar

    bit_duration = 1        # tempo por bit (em segundos)
    sampling_rate = 100     # Hz (amostras por segundo)
    samples_per_bit = bit_duration * sampling_rate

    min_len = min(len(q1), len(q2), len(q3))
    q1, q2, q3 = q1[:min_len], q2[:min_len], q3[:min_len]

    # Multiplexação TDM: intercalar os bits (um por canal)
    tdm_bits = ''
    for i in range(min_len):
        tdm_bits += q1[i] + q2[i] + q3[i]  

    return tdm_bits, samples_per_bit, bit_duration

tdm_bits, samples_per_bit, bit_duration = gerar_sinal_tdm(dados)

# Gerar sinal digital (0 ou 1) no tempo
sinal_tdm = []
for bit in tdm_bits:
    nivel = int(bit)
    sinal_tdm.extend([nivel] * int(samples_per_bit))

# Eixo do tempo
tempo_total = np.linspace(0, len(tdm_bits) * bit_duration, len(sinal_tdm), endpoint=False)

plt.figure(figsize=(16, 4))
plt.plot(tempo_total, sinal_tdm, drawstyle='steps-post', color='blue')
plt.title('Sinal Multiplexado TDM dos 3 Quadros (intercalando bits)')
plt.xlabel('Tempo (s)')
plt.ylabel('Nível lógico')
plt.ylim(-0.5, 1.5)
plt.grid(True)

# Adicionar áreas coloridas por canal para visualização
cores = ['red', 'green', 'orange']
for i in range(len(tdm_bits)):
    canal_idx = i % 3
    plt.axvspan(i * bit_duration, (i + 1) * bit_duration, facecolor=cores[canal_idx], alpha=0.1)

plt.tight_layout()
plt.show()

