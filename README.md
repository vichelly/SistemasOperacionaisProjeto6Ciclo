
# Projeto de Sistemas Operacionais

Esta atividade consiste na implementação dos algoritmos que simulam o serviço de troca de páginas do sistema operacional.
Implementação dos algoritmos de troca de páginas vistos em aula, ou seja FIFO Page Replacement, Optimal Page Replacement (OPT) e Last Recent Used Page Replacement (LRU)

## Como Executar o Programa

1. **Requisitos**:
   - Python instalado 

2. **Executar o Programa**:
   - Abra um terminal e navegue até o diretório onde o arquivo Python está localizado

3. **Executar o Script**:
   - Use o seguinte comando para executar o programa:
     ```
     py page_replacement.py
     ```

4. **Interagir com o Programa**:
   - O programa solicitará que você escolha um algoritmo de substituição de página (1, 2 ou 3):
     - **1** - FIFO Page Replacement
     - **2** - LRU Page Replacement
     - **3** - OPT Optimal Page Replacement
   - Após escolher, forneça o tamanho da memória (número de páginas) e a sequência de páginas (separadas por vírgula).

## Exemplo de Uso
```
Escolha o algoritmo de substituição de página:
1 - FIFO Page Replacement
2 - LRU Page Replacement
3 - OPT Optimal Page Replacement
Digite o número da sua escolha: 1
Digite o tamanho da memória (número de páginas): 3
Digite a sequência de páginas (separadas por vírgula): 1,2,3,1,4,2,1,5,2,1
```

## Resultados
- O programa exibirá a simulação da substituição de páginas e as estatísticas finais como hit or miss