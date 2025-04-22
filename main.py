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
from sinais_validos_grafico import plotar_3_quadros_em_linhas


# geração de dados e enquadramento
dados_originais = dados()
quadros_selecionados, indice = armazenar_dados(dados_originais)


# sinal digital dos quadros
grafico_dos_sinais_digitais = plotar_sinais_digitais(quadros_selecionados, indice)


# multiplexação
tdm_bits, samples_per_bit, bit_duration = gerar_sinal_tdm(quadros_selecionados)
grafico_tdm = plotar_sinal_tdm(quadros_selecionados, indice)
print(f'Sinal multiplexado: {tdm_bits}')


# modulações
sinal_ask, sinal_fsk, sample_per_bit, t = gerar_sinais_modulados(tdm_bits)
exibir_grafico_modulacao = grafico_modulacao(sinal_ask, sinal_fsk, t)
print(f'\nSinal modulado: {sinal_ask}')


# canal com ruido (para passar pela função com ruído foi escolhido apenas o sinal ASK)
sinal_com_ruido = injetar_ruido_ask_bitwise(sinal_ask, sample_per_bit)
print("\nSinal original:", sinal_ask)
print("Após passar por canal com ruído:", sinal_com_ruido)


# demodulação ask 
sinal_demodulado = demodular_ask(sinal_com_ruido, sample_per_bit)
print("\nBits demodulados:", sinal_demodulado)


# demultiplexação tdm
canais = demultiplexar_tdm(sinal_demodulado)
print(f'\nQuadros demultiplexados: {canais}')


# remoção das flags e unstuffing
quadros = []
for canal in canais:
    quadros += extrair_quadros(canal)
quadros_sem_stuffing = [bit_unstuffing(quadro) for quadro in quadros]


# Mostrar os quadros sem flags e stuffing
for i, quadro in enumerate(quadros_sem_stuffing):
    print(f"\nQuadro {i+1} sem stuffing e flags: {quadro}")


# verificar erro novamente com CRC
quadros_validos = []

total_quadros = min(len(quadros_sem_stuffing), len(quadros_selecionados))

for i in range(total_quadros):
    quadro = quadros_sem_stuffing[i]
    sucesso = False

    while not sucesso:
        # removendo bits de paridade
        dados_sem_crc = quadro[:-32]
        crc_recebido = quadro[-32:]

        if calcular_crc32(dados_sem_crc) == crc_recebido:
            print(f"Quadro {i+1} está correto.")
            quadros_validos.append((i, dados_sem_crc))
            sucesso = True
        else:
            print(f"\nErro detectado no Quadro {i+1}, reenviando...")

            # reenviando o quadro original com CRC correto para simulação
            quadro_original_sem_crc = bit_unstuffing(quadros_selecionados[i])[:-32]  # tira bits de paridade antigos
            quadro_reenviado = anexar_crc_manual(quadro_original_sem_crc)

            # Substituir para nova tentativa
            quadro = quadro_reenviado

# Visualização do sinal digital do quadro escolhido em 1.1.4 (sem bits de paridade)
quadros_sem_crc = [q for _, q in quadros_validos]

# Plotar até 3 quadros válidos
if len(quadros_sem_crc) >= 1:
    plotar_3_quadros_em_linhas(quadros_sem_crc)
else:
    print("[AVISO] Nenhum quadro válido disponível para plotagem.")