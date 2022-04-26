import numpy as np
import matplotlib.pyplot as plt

# Maximizar ou Minimizar
maximizar = False

# Pareto construct O(n²)
def no_dominated_simple_cull(pontos, domina):
    dominantes = set()
    idxCandidatoInicial = 0
    dominados = set()
    while True:
        candidatoInicial = pontos[idxCandidatoInicial]
        pontos.remove(candidatoInicial)
        idxCorrente = 0
        flagDominado = True
        while len(pontos) != 0 and idxCorrente < len(pontos):
            candidatoCorrente = pontos[idxCorrente]
            if domina(candidatoInicial, candidatoCorrente):
                # Caso pior nas duas caracteristica remove do conjunto
                pontos.remove(candidatoCorrente)
                dominados.add(tuple(candidatoCorrente))
            elif domina(candidatoCorrente, candidatoInicial):
                flagDominado = False
                dominados.add(tuple(candidatoInicial))
                idxCorrente += 1
            else:
                idxCorrente += 1

        if flagDominado:
            # adiciona os pontos não dominados na frente de pareto
            dominantes.add(tuple(candidatoInicial))

        if len(pontos) == 0:
            break
    return dominantes

# Dominates function
def dominates(row, candidateRow):
    if (maximizar):
        return sum([row[x] >= candidateRow[x] for x in range(len(row))]) == len(row)
    else:
        return sum([row[x] <= candidateRow[x] for x in range(len(row))]) == len(row)

# Instancia
#with open("./P_500_01.csv") as input_file:
#    arr = np.loadtxt(input_file, delimiter=",")

# Conjunto aleatorio
arr = 10*np.random.rand(1000,2)

# Imprimir coordenadas x,y dos pontos da frente de pareto encontrada
inputPoints = arr.tolist()
paretoPoints = no_dominated_simple_cull(inputPoints, dominates)
print("*"*8 + " non-dominated answers " + ("*"*8))
for p in paretoPoints:
    print(p)

# Plotar grafico com os pontos da frente de pareto em vermelho
result = list(paretoPoints)
paretoList = np.asarray(result)
plt.plot(arr[:,0],arr[:,1],'k*',paretoList[:,0],paretoList[:,1],'ro')
plt.show()