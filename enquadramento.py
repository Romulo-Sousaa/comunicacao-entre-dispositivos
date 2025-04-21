from datagramas import dados
from crc32 import calcular_crc32, anexar_crc_manual
import random

def adicionar_flag(datar):
    # Flag de início e fim
    flag = '01111110'
    return flag + datar + flag

def bit_stuffing(datar):
    
    stuffed_data = ""
    count = 0

    for bit in datar:
        stuffed_data += bit
        if bit == '1':
            count += 1
        else:
            count = 0
        
        # Se tiver 5 bits consecutivos 1, coloca um 0
        if count == 5:
            stuffed_data += '0'
            count = 0  # Reinicia a contagem de 1s consecutivos

    return stuffed_data

def bit_unstuffing(quadro_stuffado):
    unstuffed = ''
    count = 0
    i = 0
    while i < len(quadro_stuffado):
        bit = quadro_stuffado[i]
        unstuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                i += 1  # Pular o bit '0' inserido
                count = 0
        else:
            count = 0
        i += 1
    return unstuffed

def extrair_quadros(bitstream, flag='01111110', tamanho_minimo=16):
    if isinstance(bitstream, list):
        bitstream = ''.join(str(b) for b in bitstream)
    partes = bitstream.split(flag)
    quadros = [parte for parte in partes if len(parte.strip()) >= tamanho_minimo]
    return quadros

def construir_quadros(datar):
    # Dividir em 5 quadros menores
    tamanho_quadro = 200
    quadros = []
    for i in range(0, len(datar), tamanho_quadro):
        quadro = datar[i:i + tamanho_quadro]
        quadro_com_crc = anexar_crc_manual(quadro)
        quadro_stuffing = bit_stuffing(quadro_com_crc)
        quadro_final = adicionar_flag(quadro_stuffing)
        quadros.append(quadro_final)
    return quadros

def armazenar_dados(datar):
    dados_tratados = [construir_quadros(d) for d in datar]
    indice = random.randint(0, 4)
    quadros_selecionados = [datagrama[indice] for datagrama in dados_tratados]

    return quadros_selecionados, indice