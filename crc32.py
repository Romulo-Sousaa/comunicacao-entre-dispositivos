def calcular_crc32(bits):
    polinomio = int("100000100110000010001110110110111", 2)
    dados = int(bits + "0" * 32, 2)
    tamanho = len(bits) + 32
    for i in range(len(bits)):
        if (dados >> (tamanho - 1 - i)) & 1:
            dados ^= polinomio << (tamanho - 33 - i)
    crc = dados & 0xFFFFFFFF
    return f"{crc:032b}"