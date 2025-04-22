from multiplexacao_tdm import gerar_sinal_tdm

def demultiplexar_tdm(tdm_bits: str, n_canais: int = 3) -> list:
   
    canais = ['' for _ in range(n_canais)]
    for i, bit in enumerate(tdm_bits):
        canal = i % n_canais
        canais[canal] += bit
    return canais