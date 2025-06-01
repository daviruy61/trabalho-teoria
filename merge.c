#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void intercala(int inicio, int meio, int fim, int v[]) {
    int i = inicio, j = meio + 1, k = 0;
    int *aux = malloc((fim - inicio + 1) * sizeof(int));

    while (i <= meio && j <= fim) {
        if (v[i] <= v[j]) aux[k++] = v[i++];
        else              aux[k++] = v[j++];
    }
    while (i <= meio) aux[k++] = v[i++];
    while (j <= fim)  aux[k++] = v[j++];
    for (i = inicio, k = 0; i <= fim; i++, k++)
        v[i] = aux[k];

    free(aux);
}

void mergesort(int inicio, int fim, int v[]) {
    if (inicio < fim) {
        int meio = (inicio + fim) / 2;
        mergesort(inicio, meio, v);
        mergesort(meio + 1, fim, v);
        intercala(inicio, meio, fim, v);
    }
}

int main() {
    FILE *f = fopen("../casos_de_teste/melhor-caso-500k.txt", "r"); //mude o arquivo a ser ordenado aqui
    if (!f) {
        perror("Erro ao abrir arquivo");
        return EXIT_FAILURE;
    }

    const int capacidade = 1000001;
    int *v = malloc(capacidade * sizeof(int));
    if (!v) {
        perror("Erro de alocação");
        fclose(f);
        return EXIT_FAILURE;
    }

    int tamanho = 0;
    while (tamanho < capacidade && fscanf(f, "%d", &v[tamanho]) == 1)
        tamanho++;
    fclose(f);

    if (tamanho == 0) {
        fprintf(stderr, "Nenhum número lido do arquivo ou formato inválido\n");
        free(v);
        return EXIT_FAILURE;
    }

    clock_t inicio = clock();

    mergesort(0, tamanho - 1, v);

    clock_t fim = clock();

    double duracao = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo de ordenação: %.6f segundos\n", duracao);

    //printf("Vetor ordenado com %d números:\n", tamanho);
    //for (int i = 0; i < tamanho; i++)
    //    printf("%d ", v[i]);
    //printf("\n");

    free(v);
    return EXIT_SUCCESS;
}
