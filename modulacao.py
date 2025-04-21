import numpy as np

# a função abaiixo gera 75.000 amostras analógicas para ask
def gerar_sinais_modulados(sinal_multiplexado):
    # Parâmetros
    amplitude_1 = 1.0
    amplitude_0 = 0.0
    bit_duration = 1  # segundos por bit
    sampling_rate = 100  # amostras por segundo
    samples_per_bit = int(sampling_rate * bit_duration)

    t = np.linspace(0, len(sinal_multiplexado) * bit_duration, len(sinal_multiplexado) * samples_per_bit, endpoint=False)

    # ASK
    sinal_ask = np.zeros_like(t, dtype=float)
    for i, bit in enumerate(sinal_multiplexado):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        amplitude = amplitude_1 if bit == '1' else amplitude_0
        sinal_ask[start:end] = amplitude

    # FSK
    f_0 = 5  # Hz
    f_1 = 10  # Hz
    sinal_fsk = np.zeros_like(t, dtype=float)
    for i, bit in enumerate(sinal_multiplexado):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        t_bit = np.linspace(0, bit_duration, samples_per_bit, endpoint=False)
        freq = f_1 if bit == '1' else f_0
        sinal_fsk[start:end] = np.sin(2 * np.pi * freq * t_bit)

    return sinal_ask, sinal_fsk, samples_per_bit, t