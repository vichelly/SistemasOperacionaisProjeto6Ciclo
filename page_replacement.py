def fifo_page_replacement(page_size, page_sequence):
    memory = [-1] * page_size  # Inicializa a memória com -1
    page_faults = 0            # Contador de faltas de página (miss)
    page_hits = 0              # Contador de acertos de página (hit)
    next_replace_index = 0     # Índice da próxima página a ser substituída (ciclo FIFO)

    print("FIFO Page Replacement Simulation\n")

    # Processa cada página na sequência
    for page in page_sequence:
        print(f"page: {page}")

        if page in memory:
            page_hits += 1
            for i, p in enumerate(memory):
                if p == page:
                    print(f"[{p:2}] <- (hit)")
                else:
                    print(f"[{p:2}]")
        else:
            page_faults += 1
            memory[next_replace_index] = page
            for i, p in enumerate(memory):
                if i == next_replace_index:
                    print(f"[{p:2}] <- (miss)")
                else:
                    print(f"[{p:2}]")
            next_replace_index = (next_replace_index + 1) % page_size

        print("")  # Linha em branco para separar cada passo

    total_accesses = page_hits + page_faults

    print(f"Hit rate ({page_hits}/{total_accesses}):")
    print(f"Miss rate ({page_faults}/{total_accesses}):\n")


def lru_page_replacement(page_size, page_sequence):
    memory = [-1] * page_size
    page_faults = 0
    page_hits = 0
    usage_history = []

    print("LRU Page Replacement Simulation\n")

    for page in page_sequence:
        print(f"page: {page}")

        if page in memory:
            page_hits += 1
            usage_history.remove(page)
            usage_history.append(page)
            for i, p in enumerate(memory):
                if p == page:
                    print(f"[{p:2}] <- (hit)")
                else:
                    print(f"[{p:2}]")
        else:
            page_faults += 1
            if -1 in memory:
                empty_index = memory.index(-1)
                memory[empty_index] = page
                usage_history.append(page)
                for i, p in enumerate(memory):
                    if i == empty_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")
            else:
                lru_page = usage_history.pop(0)
                lru_index = memory.index(lru_page)
                memory[lru_index] = page
                usage_history.append(page)
                for i, p in enumerate(memory):
                    if i == lru_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")

        print("")

    total_accesses = page_hits + page_faults

    print(f"Hit rate ({page_hits}/{total_accesses}):")
    print(f"Miss rate ({page_faults}/{total_accesses}):\n")


def optimal_page_replacement(page_size, page_sequence):
    memory = [-1] * page_size
    page_faults = 0
    page_hits = 0

    print("Optimal Page Replacement Simulation\n")

    for current_index, page in enumerate(page_sequence):
        print(f"page: {page}")

        if page in memory:
            page_hits += 1
            for i, p in enumerate(memory):
                if p == page:
                    print(f"[{p:2}] <- (hit)")
                else:
                    print(f"[{p:2}]")
        else:
            page_faults += 1
            if -1 in memory:
                empty_index = memory.index(-1)
                memory[empty_index] = page
                for i, p in enumerate(memory):
                    if i == empty_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")
            else:
                future_uses = {}
                for i, p in enumerate(memory):
                    try:
                        future_uses[i] = page_sequence[current_index + 1:].index(p)
                    except ValueError:
                        future_uses[i] = float('inf')

                farthest_page_index = max(future_uses, key=future_uses.get)
                memory[farthest_page_index] = page
                for i, p in enumerate(memory):
                    if i == farthest_page_index:
                        print(f"[{p:2}] <- (miss)")
                    else:
                        print(f"[{p:2}]")

        print("")

    total_accesses = page_hits + page_faults

    print(f"Hit rate ({page_hits}/{total_accesses}):")
    print(f"Miss rate ({page_faults}/{total_accesses}):\n")



print("Escolha o algoritmo de substituição de página:")
print("1 - FIFO Page Replacement")
print("2 - LRU Page Replacement")
print("3 - OPT Optimal Page Replacement")
choice = input("Digite o número da sua escolha: ")
page_size = int(input("Digite o tamanho da memória (número de páginas): "))
page_sequence_input = input("Digite a sequência de páginas (separadas por vírgula): ")
#transforma as páginas numa lista
page_sequence = list(map(int, page_sequence_input.split(',')))
if choice == '1':
    fifo_page_replacement(page_size, page_sequence)
elif choice == '2':
    lru_page_replacement(page_size, page_sequence)
elif choice == '3':
    optimal_page_replacement(page_size, page_sequence)
else:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
