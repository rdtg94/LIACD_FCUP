# Wood Block Puzzle com Múltiplos Níveis de Dificuldade

Este jogo é uma implementação de um puzzle de blocos de madeira com diferentes níveis de dificuldade e vários algoritmos de Inteligência Artificial.

## Características Principais

- 4 níveis de dificuldade com tamanhos de tabuleiro aumentando progressivamente
- Múltiplos modos de jogo: manual, com sugestões de IA, ou totalmente automatizado
- Comparação de 8 algoritmos diferentes de IA para resolver o puzzle
- Tabuleiros de jogo que se adaptam ao nível de dificuldade
- Peças mais complexas nos níveis mais difíceis

## Níveis de Dificuldade

1. **Fácil** - Tabuleiro 4x4
   - Ideal para iniciantes
   - Peças simples
   - Pontuação inicial: 100 pontos

2. **Médio** - Tabuleiro 5x5
   - Dificuldade moderada
   - Inclui peças adicionais em forma de L
   - Pontuação inicial: 200 pontos

3. **Difícil** - Tabuleiro 6x6
   - Para jogadores experientes
   - Inclui peças mais complexas
   - Pontuação inicial: 300 pontos

4. **Especialista** - Tabuleiro 7x7
   - O maior desafio
   - Inclui todas as peças, incluindo peças em forma de T e Z
   - Pontuação inicial: 400 pontos

## Modos de Jogo

### 1. Jogo Normal

Neste modo, você joga manualmente no tabuleiro escolhido. O objetivo é completar linhas e colunas para ganhar pontos e capturar diamantes.

### 2. Jogo com Ajuda da IA

Você joga manualmente, mas pode solicitar sugestões de movimento da IA antes de cada jogada. Você pode escolher entre diferentes algoritmos para obter a sugestão.

Algoritmos disponíveis:
- BFS (Busca em Largura)
- DFS (Busca em Profundidade)
- UCS (Busca de Custo Uniforme)
- DLS (Busca em Profundidade Limitada)
- IDS (Aprofundamento Iterativo)
- Greedy (Busca Gulosa)
- A* (A-Estrela)
- Weighted A* (A-Estrela Ponderada)

### 3. Jogo Automático com IA

A IA joga automaticamente usando o algoritmo escolhido. Você apenas observa como ela resolve o puzzle.

### 4. Comparação de Algoritmos

Este modo executa todos os algoritmos de IA no mesmo tabuleiro inicial e compara seu desempenho em termos de:
- Tempo de execução
- Estados explorados
- Comprimento do caminho encontrado
- Se encontrou uma solução ou não

## Como Jogar

### Regras Básicas

1. Você começa com uma pontuação inicial que depende do nível de dificuldade
2. Cada movimento custa pontos (mais pontos nos níveis mais difíceis)
3. Completar linhas ou colunas ganha pontos
4. Capturar diamantes ganha pontos adicionais
5. O jogo termina quando você fica sem pontos

### Comandos

- Para posicionar uma peça, digite as coordenadas como "linha coluna" (ex: "2 3")
- Para solicitar uma nova peça, digite "R" (perderá alguns pontos)
- Para sair do jogo e voltar ao menu principal, digite "q" a qualquer momento
- Para sair completamente do jogo, digite "q" no menu principal

## Instalação e Execução

1. Certifique-se de ter Python 3.6 ou superior instalado
2. Clone ou baixe os arquivos `NOME DO FICHEIRO FINAL.py` e `NOME DO FICHEIRO FINAL DOS ALGORITMOS.py`
3. Execute o jogo com o comando:

```
python NOME DO FICHEIRO FINAL.py
```

## Dicas Estratégicas

- Nos níveis mais difíceis, considere pedir ajuda ao algoritmo A* ou Weighted A* para movimentos ótimos
- Tente completar linhas ou colunas que contenham diamantes para maximizar a pontuação
- Evite solicitar novas peças desnecessariamente, pois isso diminui sua pontuação
- Nos tabuleiros maiores, comece preenchendo a partir dos cantos para aumentar suas chances de completar múltiplas linhas/colunas
