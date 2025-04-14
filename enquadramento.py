from datagramas import dados
from crc32 import calcular_crc32

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

def construir_quadros(datar):
    # Dividir em quadros menores
    tamanho_quadro = 200
    quadros = []
    for i in range(0, len(datar), tamanho_quadro):
        quadro = datar[i:i + tamanho_quadro]
        quadro_stuffing = bit_stuffing(quadro)
        crc = calcular_crc32(quadro_stuffing)
        quadro_final = adicionar_flag(quadro_stuffing + crc)
        quadros.append(quadro_final)
    return quadros

datagramas = dados()

for i, datagrama in enumerate(datagramas, 1):
    quadros = construir_quadros(datagrama)
    print(f"\n🧩 Datagrama {i} dividido em {len(quadros)} quadros com CRC-32:")
    for j, quadro in enumerate(quadros, 1):
        print(f"  Quadro {j}: {quadro}")