# Campo magnético resultante de um motor assíncrono de indução trifásico.
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
# Frequência angular
freq = 60
w = 2 * np.pi * freq

# Vetor de tempo que varia de 0 a 0,02 segundos com um total de 10^3 pontos.
# Número de pontos escolhido para maior velocidade de execução, 10^6 leva 16s para plotar o gráfico.
t = np.linspace(0, 0.02, 10**3)

# Funções lambda para as componentes real e imaginária do campo magnético.
# As funções lambda são utilizadas quando se precisa de uma pequena função anônima,
# para uma tarefa específica, evitando a definição de uma função completa com um nome.
# Neste caso o lambda esta em função do tempo e do ângulo.
# Funciona mais ou menos como um laço for que faz a interação com o campo magnético.
Comp_real = lambda t, angulo: np.sum(
    [np.sin(w * t + a) * np.cos(a) for a in angulo], axis=0
)
Comp_imag = lambda t, angulo: np.sum(
    [np.sin(w * t + a) * np.sin(a) for a in angulo], axis=0
)

# Lista de listas que criam a combinação de ângulos solicitados
defasagens = [
    [0, np.radians(-120), np.radians(120)],
    [0, np.radians(-100), np.radians(120)],
    [0, np.radians(-150), np.radians(150)],
    [0, np.radians(-90), np.radians(150)],
]

colors = ["red", "yellow", "blue", "orange"]

# Gráficos
plt.figure()

# O loop percorre cada combinação de ângulos e usa as funções lambda,
# para calcular as componentes real e imaginária do campo magnético.
for angulo, color in zip(defasagens, colors):
    plt.plot(
        Comp_real(t, angulo),
        Comp_imag(t, angulo),
        color=color,
        label=f"Ângulos = {angulo}",
    )

plt.title("Campo Magnético Resultante no Estator")
plt.xlabel("Componente Real")
plt.ylabel("Componente Imaginária")
plt.grid(True)
plt.legend(loc="best", fontsize=6)
plt.show()
