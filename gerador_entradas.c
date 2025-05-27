// gera_entrada_interativo.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main() {
    long quantidade;
    char nome_arquivo[256];
    char caminho[512];

    // Pergunta pelo tamanho
    printf("Qual o tamanho da entrada desejada? (entre 100000 e 1000000): ");
    if (scanf("%ld", &quantidade) != 1) {
        fprintf(stderr, "Entrada inválida.\n");
        return EXIT_FAILURE;
    }
    if (quantidade < 100000 || quantidade > 1000000) {
        fprintf(stderr, "Quantidade fora do intervalo permitido.\n");
        return EXIT_FAILURE;
    }

    // Limpa o buffer antes de ler a string
    getchar();

    // Pergunta pelo nome do arquivo
    printf("Qual o nome do arquivo (ex: teste100000.txt): ");
    if (fgets(nome_arquivo, sizeof(nome_arquivo), stdin) == NULL) {
        fprintf(stderr, "Não foi possível ler o nome do arquivo.\n");
        return EXIT_FAILURE;
    }
    // Remove eventual '\n'
    nome_arquivo[strcspn(nome_arquivo, "\r\n")] = '\0';

    // Monta o caminho completo
    snprintf(caminho, sizeof(caminho), "../casos_de_teste/%s", nome_arquivo);

    // Abre para escrita
    FILE *f = fopen(caminho, "w");
    if (!f) {
        perror("Erro ao criar o arquivo");
        return EXIT_FAILURE;
    }

    // Inicializa gerador
    srand((unsigned) time(NULL));

    // Gera os números
    for (long i = 0; i < quantidade; i++) {
        int valor = rand() % 999 + 1;  // gera [1, 999]
        fprintf(f, "%d\n", valor);
    }

    fclose(f);
    printf("Arquivo '%s' criado com %ld números.\n", caminho, quantidade);
    return EXIT_SUCCESS;
}
