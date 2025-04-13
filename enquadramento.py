from datagramas import dados

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

def dividir_datagrama(datar):
    # Tratando os dados com bit stuffing
    datar_com_stuffing = bit_stuffing(datar)
    
    # Adicionar flags de início e fim
    datar_com_flags = adicionar_flag(datar_com_stuffing)
    
    return datar_com_flags

datagrama = dados()[0]

# Dividir datagrama com bit stuffing e flags
datagrama_dividido = dividir_datagrama(datagrama)
print(datagrama_dividido)
