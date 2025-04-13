import random

def gerar_kbit():
    return ''.join(random.choice(['0', '1']) for _ in range(1000))

# Gerar os 3 conjuntos
def dados():
    return [gerar_kbit() for _ in range(3)]