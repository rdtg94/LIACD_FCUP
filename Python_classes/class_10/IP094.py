def read_input():
    global r, c, k, grid
    r, c, k = map(int, input().split())
    # Ler a grid como list of lists
    grid = [list(input().strip()) for _ in range(r)]

def count_live_neighbors(grid, x, y):
    # Definir oito direções possíveis para os vizinhos
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    live_neighbors = 0
    # Verificar cada vizinho e contar os vivos
    for dx, dy in directions:
        # Calcular as coordenadas do vizinho
        nx, ny = x + dx, y + dy
        # Verificar se o vizinho está dentro do tabuleiro e se está vivo
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '#':
            live_neighbors += 1
    return live_neighbors

def next_generation(grid):
    # Criar um novo tabuleiro vazio para a próxima geração
    new_grid = [['.' for _ in range(c)] for _ in range(r)]
    # Para cada célula do tabuleiro atual verificar se ela sobrevive ou nasce na próxima geração
    for i in range(r):
        for j in range(c):
            # Contar os vizinhos vivos da célula atual (i, j)
            live_neighbors = count_live_neighbors(grid, i, j)
            # Verificar se a célula atual sobrevive ou nasce na próxima geração
            if grid[i][j] == '#' and (live_neighbors == 2 or live_neighbors == 3):
                # A célula sobrevive se tiver 2 ou 3 vizinhos vivos
                new_grid[i][j] = '#'
                # A célula nasce se tiver exatamente 3 vizinhos vivos e estava morta
            elif grid[i][j] == '.' and live_neighbors == 3:
                new_grid[i][j] = '#'
            else:
                # A célula morre se tiver menos de 2 ou mais de 3 vizinhos vivos ou se estiver morta e não tiver 3 vizinhos vivos
                new_grid[i][j] = '.'
    return new_grid

def simulate():
    global grid
    # Simular K gerações do jogo
    for _ in range(k):
        grid = next_generation(grid)

def print_grid(grid):
    for row in grid:
        print(''.join(row))

# Main code
read_input()
simulate()
print_grid(grid)