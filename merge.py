def intercala(inicio, meio, fim, v):

    esquerda = v[inicio:meio+1]
    direita = v[meio+1:fim+1]
    
    i, j, k = 0, 0, inicio
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            v[k] = esquerda[i]
            i += 1
        else:
            v[k] = direita[j]
            j += 1
        k += 1
    
    while i < len(esquerda):
        v[k] = esquerda[i]
        i += 1
        k += 1
    
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

    tamanho = int(input("Digite o tamanho do vetor: "))
    
    v = []
    print("Digite os elementos do vetor:")
    for _ in range(tamanho):
        v.append(int(input()))

    print("Vetor desordenado:")
    print(*v)

    mergesort(0, tamanho - 1, v)

    print("Vetor ordenado:")
    print(*v)

if __name__ == "__main__":
    main()
