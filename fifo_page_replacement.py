# Algoritmo de substituição de páginas FIFO sem ponteiros e sem bibliotecas

def fifo_page_replacement(page_size, page_sequence):
    memory = [-1] * page_size  # Inicializa a memória com -1 (indica posições vazias)
    page_faults = 0            # Contador de faltas de página (miss)
    page_hits = 0              # Contador de acertos de página (hit)
    next_replace_index = 0     # Índice da próxima página a ser substituída (ciclo FIFO)

    print("FIFO Page Replacement Simulation\n")

    # Processa cada página na sequência
    for page in page_sequence:
        print(f"page: {page}")

        # Verifica se a página já está na memória
        if page in memory:
            # A página já está na memória, então é um hit
            page_hits += 1
            for i, p in enumerate(memory):
                if p == page:
                    print(f"[{p:2}] <- (hit)")
                else:
                    print(f"[{p:2}]")
        else:
            # A página não está na memória, então é um miss
            page_faults += 1

            # Insere a nova página no índice da próxima substituição (ciclo FIFO)
            memory[next_replace_index] = page
            for i, p in enumerate(memory):
                if i == next_replace_index:
                    print(f"[{p:2}] <- (miss)")
                else:
                    print(f"[{p:2}]")

            # Atualiza o índice da próxima substituição
            next_replace_index = (next_replace_index + 1) % page_size

        print("")  # Linha em branco para separar cada passo

    # Exibe as estatísticas finais
    total_accesses = page_hits + page_faults
    miss_rate = (page_faults / total_accesses) * 100
    hit_rate = (page_hits / total_accesses) * 100

    print("--- Final Statistics ---")
    print(f"Hit rate ({page_hits}/{total_accesses}): {hit_rate:.2f}%")
    print(f"Miss rate ({page_faults}/{total_accesses}): {miss_rate:.2f}%")

# Solicitando entrada do usuário
page_size = int(input("Digite o tamanho da memória (número de páginas): "))
page_sequence_input = input("Digite a sequência de páginas (separadas por vírgula): ")

# Convertendo a sequência de páginas em uma lista de inteiros
page_sequence = list(map(int, page_sequence_input.split(',')))

# Chama a função com os parâmetros fornecidos
fifo_page_replacement(page_size, page_sequence)
