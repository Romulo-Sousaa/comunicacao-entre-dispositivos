from datagramas import dados
from enquadramento import armazenar_dados, extrair_quadros, bit_unstuffing
from sinal_digital_grafico import plotar_sinais_digitais
from multiplexacao_tdm import gerar_sinal_tdm, plotar_sinal_tdm
from modulacao import gerar_sinais_modulados
from modulacao_graficos import grafico_modulacao
from injetar_ruido import injetar_ruido_ask_bitwise
from demodulacao import demodular_ask, gerar_demodulacoes_ask
from demultiplexacao import demultiplexar_tdm
from crc32 import calcular_crc32, anexar_crc_manual, verificar_crc_manual


# geração de dados e enquadramento
dados_originais = dados()
quadros_selecionados, indice = armazenar_dados(dados_originais)


# sinal digital dos quadros
# grafico_dos_sinais_digitais = plotar_sinais_digitais(quadros_selecionados, indice)


# multiplexação
tdm_bits, samples_per_bit, bit_duration = gerar_sinal_tdm(quadros_selecionados)
# grafico_tdm = plotar_sinal_tdm(quadros_selecionados, indice)


# modulações
sinal_ask, sinal_fsk, sample_per_bit, t = gerar_sinais_modulados(tdm_bits)
# exibir_grafico_modulacao = grafico_modulacao(sinal_ask, sinal_fsk, t)


# canal com ruido
sinal_com_ruido = injetar_ruido_ask_bitwise(sinal_ask, sample_per_bit)
print("Original:", sinal_ask)
print("Com ruído:", sinal_com_ruido)


# demodulação ask 
sinal_demodulado = demodular_ask(sinal_com_ruido, sample_per_bit)
print("Bits demodulados:", sinal_demodulado)


# demultiplexação tdm
canais = demultiplexar_tdm(sinal_demodulado)
print(f'\nQuadros demultiplexados: {canais}')


# remoção das flags e unstuffing
quadros = []
for canal in canais:
    quadros += extrair_quadros(canal)
quadros_sem_stuffing = [bit_unstuffing(quadro) for quadro in quadros]

# Mostrar os quadros sem stuffing
for i, quadro in enumerate(quadros_sem_stuffing):
    print(f"Quadro {i+1} sem stuffing: {quadro}")


# verificar erro novamente com CRC
quadros_com_erro_indices = []
for i, quadro in enumerate(quadros_sem_stuffing):
    dados_sem_crc = quadro[:-32]
    crc_recebido = quadro[-32:]
    if calcular_crc32(dados_sem_crc) == crc_recebido:
        print(f"Quadro {i+1} está correto.")
    else:
        print(f"Erro detectado no Quadro {i+1}.")
        quadros_com_erro_indices.append(i)