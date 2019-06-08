import numpy as np

def calcCarga(vetor):
    # print(vetor)
    carga = 0
    ordenado = np.sort(vetor)
    while (len(vetor) > 2):
        tiraveis = []
        tiraveisindex = []
        for i in range(len(vetor)):
            if i != 0 and i+1 != len(vetor):
                esq = vetor[i-1]
                direita = vetor[i+1]
                if np.where(ordenado == esq)[0][0] < np.where(ordenado == direita)[0][0]:
                    tiraveis.append(esq)
                    tiraveisindex.append(i)
                else:
                    tiraveis.append(direita)
                    tiraveisindex.append(i)


        # print("Vetor de cargas", tiraveis)
        # pega o valor maximo no vetor de tiraveis
        maximum = np.amax(tiraveis)

        # pega o indice do valor tiravel no vetor de tiraveis
        indicetiravel = np.where(tiraveis == maximum)

        # verifica se o maior numero tiravel se repete mais de uma vez
        # caso sim, verifica qual o melhor indice para poder tirá-lo (o menor número que posso tirar do vetor)
        indice = 0
        if len(indicetiravel[0]) > 1:
            maior = vetor[tiraveisindex[indicetiravel[0][0]]]

            for i in range(len(indicetiravel[0])):
                if vetor[tiraveisindex[indicetiravel[0][i]]] > maior:
                    maior = vetor[tiraveisindex[indicetiravel[0][i]]]
                    indice = i

        #   Determino o indice, no vetor original, que será retirado 
            indiceTiravelOriginal = tiraveisindex[indicetiravel[0][indice]]

        else:
            indiceTiravelOriginal = tiraveisindex[indicetiravel[0][0]]

        indiceCarga = indicetiravel[0][indice]
        # print("Indice no vetor de cargas:", indiceCarga, "Indice tirado no original:", indiceTiravelOriginal, " Valor tirado:", vetor[indiceTiravelOriginal])
        
        del vetor[indiceTiravelOriginal]
        
        # print(vetor)
        carga += tiraveis[indiceCarga]
        

    return carga

def main():
    # vetor = [1, 2, 3, 4, 5]
    # vetor = [10, 2, 7, 6, 8, 3]
    # vetor = [6, 4, 5, 1, 6, 2, 5]
    # vetor = [2, 4, 2, 6, 4, 6]
    vetor = [3, 2, 1, 1, 3, 2, 1]

    print(calcCarga(vetor))

if __name__ == '__main__':
    main()