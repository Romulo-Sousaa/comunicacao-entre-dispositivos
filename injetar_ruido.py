import numpy as np
import random

def injetar_ruido_ask_bitwise(sinal_ask, samples_per_bit, pr=0.01):
 
    sinal_ruidoso = np.copy(sinal_ask)
    num_bits = len(sinal_ask) // samples_per_bit

    for i in range(num_bits):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit

        if random.random() < pr:
            # Flipar o bit inteiro: 1.0 ↔ 0.0
            bit_valor_medio = np.mean(sinal_ruidoso[start:end])
            novo_valor = 0.0 if bit_valor_medio > 0.5 else 1.0
            sinal_ruidoso[start:end] = novo_valor

    return sinal_ruidoso