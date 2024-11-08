def lru_page_replacement(page_size, page_sequence):
    # Inicializa a memória com -1 para indicar posições vazias
    memory = [-1] * page_size
    page_faults = 0  # Contador de faltas de página (miss)
    page_hits = 0    # Contador de acertos de página (hit)
    usage_history = []  # Lista para armazenar a ordem de uso das páginas

    print("LRU Page Replacement Simulation\n")

    # Processa cada página na sequência
    for page in page_sequence:
        print(f"page: {page}")

        if page in memory:
            # A página já está na memória, então é um hit
            page_hits += 1
            usage_history.remove(page)  # Atualiza o histórico de uso
            usage_history.append(page)
            for i, p in enumerate(memory):
                if p == page:
                    print(f"[{p:2}] <- (hit)")
                else:
                    print(f"[{p:2}]")
        else:
            # A página não está na memória, então é um miss
            page_faults += 1

            if -1 in memory:
                # Ainda há espaço na memória (indicado por -1), então adiciona a página
                empty_index = memory.index(-1)
                memory[empty_index] = page
                usage_history.append(page)
                for i, p in enumerate(memory):
                    if i == empty_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")
            else:
                # Memória cheia, precisa substituir uma página
                # A página menos recentemente usada é a primeira do histórico
                lru_page = usage_history.pop(0)
                lru_index = memory.index(lru_page)
                memory[lru_index] = page
                usage_history.append(page)
                for i, p in enumerate(memory):
                    if i == lru_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")

        print("")  # Linha em branco para separar cada passo

    # Exibe as estatísticas finais
    total_accesses = page_hits + page_faults
    miss_rate = (page_faults / total_accesses) * 100 if total_accesses > 0 else 0
    hit_rate = (page_hits / total_accesses) * 100 if total_accesses > 0 else 0

    print("--- Final Statistics ---")
    print(f"Hit rate ({page_hits}/{total_accesses}): {hit_rate:.2f}%")
    print(f"Miss rate ({page_faults}/{total_accesses}): {miss_rate:.2f}%")

# Função principal para capturar a entrada do usuário
def main():
    # Solicita entrada do usuário
    page_size = int(input("Digite o tamanho da memória (número de páginas): "))
    page_sequence_input = input("Digite a sequência de páginas (separadas por vírgula): ")

    # Convertendo a sequência de páginas em uma lista de inteiros
    page_sequence = list(map(int, page_sequence_input.split(',')))

    # Executa o algoritmo LRU
    lru_page_replacement(page_size, page_sequence)

if __name__ == "__main__":
    main()
