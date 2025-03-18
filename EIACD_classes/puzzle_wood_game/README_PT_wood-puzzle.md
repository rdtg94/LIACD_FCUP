# Wood Block Puzzle

## Português (PT-PT)

### Visão Geral
Wood Block Puzzle é um jogo de quebra-cabeça baseado em Python onde os jogadores colocam blocos de madeira numa grelha para completar linhas e colunas. O jogo inclui vários níveis de dificuldade, jogabilidade assistida por IA e diversos algoritmos de IA que podem ser utilizados para jogo automático ou comparação.

### Características
- Múltiplos níveis de dificuldade (Fácil, Médio, Difícil, Especialista)
- Tamanhos variáveis de tabuleiro (4x4, 5x5, 6x6, 7x7)
- Diferentes formas de peças baseadas na dificuldade
- Diamantes para pontos bónus
- Mecânica de limpeza de linhas e colunas
- Múltiplos modos de jogo:
  - Jogabilidade normal
  - Jogabilidade assistida por IA
  - Jogo automático por IA
  - Comparação de algoritmos de IA

### Instalação
1. Certifique-se que tem Python 3.x instalado
2. Descarregue os ficheiros do jogo:
   - `WoodPuzzle_1_4.py` - Ficheiro principal do jogo
   - `AI_algorithms_1_4.py` - Ficheiro de implementação da IA
3. Não são necessárias dependências adicionais para a jogabilidade básica

### Regras do Jogo
- Comece com um tabuleiro vazio com alguns obstáculos e diamantes
- Coloque peças no tabuleiro para completar linhas e colunas
- Quando uma linha ou coluna está completamente preenchida, é limpa e ganha pontos
- Capturar diamantes em linhas/colunas limpas dá pontos bónus
- Cada movimento custa pontos baseados no nível de dificuldade
- Pode solicitar uma nova peça ao custo de pontos
- O jogo termina quando a sua pontuação chega a zero

### Como Jogar
1. Execute o jogo com o comando: `python WoodPuzzle_1_4.py`
2. No menu principal, selecione uma das seguintes opções:
   - Jogar jogo normal
   - Jogar com ajuda de IA
   - Deixar a IA jogar automaticamente
   - Comparar algoritmos de IA
3. Selecione um nível de dificuldade (1-4)
4. Siga as instruções no ecrã para jogar

#### Controlos do Jogo Normal
- Introduza as coordenadas da linha e coluna (ex: `2 3`) para colocar uma peça
- Introduza `R` para solicitar uma nova peça
- Introduza `q` para regressar ao menu principal

### Níveis de Dificuldade
1. **Fácil (tabuleiro 4x4)**
   - Formas de peças simples
   - Penalizações mais baixas por movimentos
   - Tabuleiro mais pequeno
2. **Médio (tabuleiro 5x5)**
   - Mais peças complexas disponíveis
   - Penalizações aumentadas
3. **Difícil (tabuleiro 6x6)**
   - Peças ainda mais complexas
   - Penalizações mais elevadas
   - Tabuleiro maior
4. **Especialista (tabuleiro 7x7)**
   - Todas as formas de peças disponíveis
   - Penalizações máximas
   - Tabuleiro de maior dimensão

### Sistema de Pontuação
- A pontuação inicial depende da dificuldade (100-400 pontos)
- Cada movimento custa pontos (escalados pela dificuldade)
- Solicitar uma nova peça custa pontos
- Limpar linhas e colunas ganha pontos
- Capturar diamantes dá pontos bónus

### Algoritmos de IA
O jogo inclui vários algoritmos de busca de IA para jogo automático:

1. **Breadth-First Search (BFS)**
   - Explora todos os estados na mesma profundidade antes de avançar
   - Garante encontrar o caminho mais curto até ao objetivo
   
2. **Depth-First Search (DFS)**
   - Explora um ramo até ao fim antes de retroceder
   - Pode encontrar uma solução rapidamente, mas não necessariamente ótima
   
3. **Uniform Cost Search (UCS)**
   - Expande estados por ordem de menor custo
   - Garante encontrar a solução ótima
   
4. **Depth-Limited Search (DLS)**
   - DFS com um limite máximo de profundidade
   - Evita caminhos de busca infinitos
   
5. **Iterative Deepening Search (IDS)**
   - Combina vantagens de BFS e DFS
   - Garante encontrar o caminho mais curto utilizando menos memória
   
6. **Greedy Search**
   - Utiliza uma heurística para estimar a distância até ao objetivo
   - Prioriza estados que parecem mais próximos da solução
   
7. **A* (A-Star) Search**
   - Combina custo do caminho e heurística
   - Garante solução ótima se a heurística for admissível
   
8. **Weighted A* Search**
   - Variação do A* que dá mais peso à heurística
   - Pode encontrar uma solução mais rapidamente à custa da otimalidade

### Jogar com Ajuda de IA
1. Selecione "Jogar com ajuda de IA" no menu principal
2. Escolha um nível de dificuldade
3. Em cada turno, pode solicitar uma sugestão da IA
4. Selecione qual algoritmo deseja utilizar para a sugestão
5. A IA recomendará um movimento que pode escolher seguir ou ignorar

### Deixar a IA Jogar Automaticamente
1. Selecione "Deixar a IA jogar automaticamente" no menu principal
2. Escolha um nível de dificuldade
3. Selecione qual algoritmo deseja que a IA utilize
4. Observe enquanto a IA joga automaticamente
5. Pressione Enter para avançar para o próximo movimento ou 'q' para sair

### Comparar Algoritmos de IA
1. Selecione "Comparar algoritmos de IA" no menu principal
2. Escolha um nível de dificuldade
3. O programa executará todos os algoritmos de IA no mesmo puzzle
4. Os resultados mostram quais algoritmos encontraram soluções, comprimentos do caminho, estados explorados e tempo gasto

