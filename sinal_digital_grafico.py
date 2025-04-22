import matplotlib.pyplot as plt

def gerar_sinal(bits):
    
    tempo = []
    nivel = []

    for i, bit in enumerate(bits):
        tempo.extend([i, i+1])
        nivel.extend([int(bit), int(bit)])

    return tempo, nivel

def plotar_sinais_digitais(dados, indice=0):
    
    plt.figure(figsize=(12, 6))
    cores = ['blue', 'green', 'red']
    
    for i, bits in enumerate(dados):
        t, n = gerar_sinal(bits)
        plt.step(t, [ni + 2*i for ni in n], where='post', label=f'Datagrama {i+1}', color=cores[i % len(cores)])

    plt.ylim(-1, 2*len(dados) + 1)
    plt.yticks([])
    plt.xlabel('Tempo')
    plt.title(f'Sinais Digitais - Quadro {indice + 1} dos {len(dados)} Datagramas')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()