def intercala(inicio, meio, fim, v):
    # Cria vetores auxiliares
    esquerda = v[inicio:meio+1]
    direita = v[meio+1:fim+1]
    
    # Índices para a mesclagem
    i, j, k = 0, 0, inicio
    
    # Mescla os dois subvetores
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1
    
    # Copia os elementos restantes do subvetor esquerdo
    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1
    
    # Copia os elementos restantes do subvetor direito
    while j < len(direita):
        v[k] = direita[j]
        j += 1
        k += 1

def mergesort(inicio, fim, v):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort(inicio, meio, v)
        mergesort(meio + 1, fim, v)
        intercala(inicio, meio, fim, v)

def main():
    # Lê o tamanho do vetor
    tamanho = int(input("Digite o tamanho do vetor: "))
    
    # Lê os elementos do vetor
    v = []
    print("Digite os elementos do vetor:")
    for _ in range(tamanho):
        v.append(int(input()))

    # Exibe o vetor desordenado
    print("Vetor desordenado:")
    print(*v)

    # Ordena usando Merge Sort
    mergesort(0, tamanho - 1, v)

    # Exibe o vetor ordenado
    print("Vetor ordenado:")
    print(*v)

if __name__ == "__main__":
    main()
