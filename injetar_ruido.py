import random
from datagramas import dados
from enquadramento import armazenar_dados
from multiplexacao_tdm import gerar_sinal_tdm

dados_originais = dados()
dados, indice = armazenar_dados(dados_originais)

def injetar_ruido(bits: str, pr: float = 0.01) -> str:
    
    bits_com_ruido = []
    for bit in bits:
        if random.random() < pr:
            # Flipar o bit
            bits_com_ruido.append('1' if bit == '0' else '0')
        else:
            bits_com_ruido.append(bit)
    return ''.join(bits_com_ruido)

tdm_bits, samples_per_bit, bit_duration = gerar_sinal_tdm(dados)
ruidoso = injetar_ruido(tdm_bits, pr=0.1) 

print("Original:", tdm_bits)
print("Com ruído:", ruidoso)
