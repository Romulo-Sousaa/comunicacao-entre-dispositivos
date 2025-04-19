import matplotlib.pyplot as plt
from datagramas import dados
from enquadramento import armazenar_dados

dados_originais = dados()

dados, indice = armazenar_dados(dados_originais)

def gerar_sinal(bits):
    # Cria arrays para tempo e nível lógico
    tempo = []
    nivel = []

    for i, bit in enumerate(bits):
        tempo.extend([i, i+1])
        nivel.extend([int(bit), int(bit)])

    return tempo, nivel

# Plotar os três sinais
plt.figure(figsize=(12, 6))
cores = ['blue', 'green', 'red']
for i, bits in enumerate(dados):
    t, n = gerar_sinal(bits)
    plt.step(t, [ni + 2*i for ni in n], where='post', label=f'Datagrama {i+1}')

plt.ylim(-1, 7)
plt.yticks([])
plt.xlabel('Tempo')
plt.title(f'Sinais Digitais - Quadro {indice + 1} dos 3 Datagramas')
plt.legend()
plt.grid(True)
plt.show()