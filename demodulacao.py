import numpy as np
from modulacao import gerar_sinais_modulados

# ASK 


def demodular_ask(sinal, samples_por_bit, threshold=0.3):

    bits = ''
    for i in range(0, len(sinal), samples_por_bit):
        trecho = sinal[i:i+samples_por_bit]
        energia = np.mean(np.abs(trecho))  # Energia/amplitude média
        bits += '1' if energia > threshold else '0'
    return bits

def gerar_demodulacoes_ask(sinais_ask, samples_per_bit):

    demodulacoes_ask = []
    for sinal in sinais_ask:
        bits = demodular_ask(sinal, samples_per_bit)
        demodulacoes_ask.append(bits)

    return demodulacoes_ask 



# FSK 


def demodular_fsk(sinal, samples_por_bit, freq0, freq1, fs):
    
    bits = ''
    t = np.arange(samples_por_bit) / fs
    onda0 = np.sin(2 * np.pi * freq0 * t)
    onda1 = np.sin(2 * np.pi * freq1 * t)

    for i in range(0, len(sinal), samples_por_bit):
        trecho = sinal[i:i+samples_por_bit]
        correlação_0 = np.dot(trecho, onda0)
        correlação_1 = np.dot(trecho, onda1)
        bits += '0' if abs(correlação_0) > abs(correlação_1) else '1'
    return bits

def gerar_demodulacoes_fsk(sinais_fsk, samples_per_bit):
    
    f0 = 5    # Hz
    f1 = 10   # Hz
    fs = 100  # taxa de amostragem (Hz)

    demodulacoes_fsk = []
    for sinal in sinais_fsk:
        bits = demodular_fsk(sinal, samples_per_bit, f0, f1, fs)
        demodulacoes_fsk.append(bits)

    return demodulacoes_fsk

