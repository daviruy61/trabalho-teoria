import time
import sys

def intercala(v, inicio, meio, fim):
    """Intercala as sublistas v[inicio:meio+1] e v[meio+1:fim+1]."""
    esquerda = v[inicio:meio+1]
    direita = v[meio+1:fim+1]
    i = j = 0
    k = inicio

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

def mergesort(v, inicio, fim):
    """Ordena v[inicio:fim+1] recursivamente."""
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort(v, inicio, meio)
        mergesort(v, meio + 1, fim)
        intercala(v, inicio, meio, fim)

def main():
    filename = "../trabalho-teoria/casos_de_teste/melhor-caso-100k.txt" 
    capacidade = 1_000_000

    try:
        with open(filename, "r") as f:
            v = []
            for linha in f:
                if len(v) >= capacidade:
                    break
                for token in linha.split():
                    if len(v) >= capacidade:
                        break
                    try:
                        v.append(int(token))
                    except ValueError:
                        print(f"Aviso: formato inválido em '{token}', pulando.", file=sys.stderr)
    except OSError as e:
        print(f"Erro ao abrir arquivo: {e}", file=sys.stderr)
        sys.exit(1)

    if not v:
        print("Nenhum número lido do arquivo ou formato inválido.", file=sys.stderr)
        sys.exit(1)

    # Ordenação e medição de tempo
    inicio = time.perf_counter()
    mergesort(v, 0, len(v) - 1)
    fim = time.perf_counter()

    duracao = fim - inicio
    print(f"Tempo de ordenação: {duracao:.6f} segundos")

    # Se quiser ver o vetor ordenado, descomente:
    # print(f"Vetor ordenado com {len(v)} números:")
    # print(" ".join(map(str, v)))

if __name__ == "__main__":
    main()
