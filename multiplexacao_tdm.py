import numpy as np
import matplotlib.pyplot as plt

def gerar_sinal_tdm(quadros):
    bit_duration = 1        # tempo por bit (em segundos)
    sampling_rate = 100     # Hz (amostras por segundo)
    samples_per_bit = bit_duration * sampling_rate

    # Preenche todos os quadros com zeros à direita até o tamanho do maior
    max_len = max(len(q) for q in quadros)
    quadros_preenchidos = [q.ljust(max_len, '0') for q in quadros]

    # Multiplexa intercalando bits dos quadros
    tdm_bits = ''
    for i in range(max_len):
        for q in quadros_preenchidos:
            tdm_bits += q[i]

    return tdm_bits, samples_per_bit, bit_duration




def plotar_sinal_tdm(dados, indice=None):
 
    tdm_bits, samples_per_bit, bit_duration = gerar_sinal_tdm(dados)

    sinal_tdm = []
    for bit in tdm_bits:
        sinal_tdm.extend([int(bit)] * int(samples_per_bit))

    tempo_total = np.linspace(0, len(tdm_bits) * bit_duration, len(sinal_tdm), endpoint=False)

    plt.figure(figsize=(16, 4))
    plt.plot(tempo_total, sinal_tdm, drawstyle='steps-post', color='blue')

    titulo = 'Sinal Multiplexado TDM dos 3 Quadros'
    if indice is not None:
        titulo += f' (Datagrama {indice + 1})'
    plt.title(titulo)
    
    plt.xlabel('Tempo (s)')
    plt.ylabel('Nível lógico')
    plt.ylim(-0.5, 1.5)
    plt.grid(True)

    cores = ['red', 'green', 'orange']
    for i in range(len(tdm_bits)):
        canal_idx = i % 3
        plt.axvspan(i * bit_duration, (i + 1) * bit_duration, facecolor=cores[canal_idx], alpha=0.1)

    plt.tight_layout()
    plt.show()