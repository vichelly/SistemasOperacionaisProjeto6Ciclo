def optimal_page_replacement(page_size, page_sequence):
    # Inicializa a memória com -1 para indicar posições vazias
    memory = [-1] * page_size
    page_faults = 0  # Contador de faltas de página (miss)
    page_hits = 0    # Contador de acertos de página (hit)

    print("Optimal Page Replacement Simulation\n")

    # Processa cada página na sequência
    for current_index, page in enumerate(page_sequence):
        print(f"page: {page}")
        
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

            # Se há uma posição vazia, coloca a página nela
            if -1 in memory:
                empty_index = memory.index(-1)
                memory[empty_index] = page
                for i, p in enumerate(memory):
                    if i == empty_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")
            else:
                # Encontrar a página na memória que será usada mais tarde (ou nunca mais)
                future_uses = {}
                for i, p in enumerate(memory):
                    try:
                        future_uses[i] = page_sequence[current_index + 1:].index(p)
                    except ValueError:
                        # Página não será mais usada
                        future_uses[i] = float('inf')
                
                # Escolher a página que será usada mais tarde ou nunca
                farthest_page_index = max(future_uses, key=future_uses.get)
                memory[farthest_page_index] = page
                for i, p in enumerate(memory):
                    if i == farthest_page_index:
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

    # Executa o algoritmo Optimal Page Replacement
    optimal_page_replacement(page_size, page_sequence)

if __name__ == "__main__":
    main()
