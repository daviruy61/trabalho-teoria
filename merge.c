#include <stdio.h>
#include <stdlib.h>

void intercala(int inicio, int meio, int fim, int v[]) {
    int i = inicio;
    int j = meio + 1;
    int k = 0;
    int *aux = (int *)malloc((fim - inicio + 1) * sizeof(int));

    while (i <= meio && j <= fim) {
        if (v[i] <= v[j]) {
            aux[k++] = v[i++];
        } else {
            aux[k++] = v[j++];
        }
    }

    while (i <= meio) {
        aux[k++] = v[i++];
    }

    while (j <= fim) {
        aux[k++] = v[j++];
    }

    for (i = inicio, k = 0; i <= fim; i++, k++) {
        v[i] = aux[k];
    }

    free(aux);
}

// Merge Sort
void mergesort(int inicio, int fim, int v[]) {
    if (inicio < fim) {
        int meio = (inicio + fim) / 2;
        mergesort(inicio, meio, v);
        mergesort(meio + 1, fim, v);
        intercala(inicio, meio, fim, v);
    }
}

int main() {
    int tamanho;
    
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);

    int v[tamanho];
    printf("Digite os elementos do vetor:\n");
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &v[i]);
    }

    printf("Vetor desordenado:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    // Merge Sort
    mergesort(0, tamanho - 1, v);

    printf("Vetor ordenado:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");

    return 0;
}
