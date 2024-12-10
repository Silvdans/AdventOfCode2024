import sys

# Read the input file
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[int(c) for c in row] for row in L]

# Directions for movement
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def dfs(x, y, G, visited):
    rows = len(G)
    cols = len(G[0])
    stack = [(x, y)]
    reachable_nines = set()

    while stack:
        cx, cy = stack.pop()
        if G[cx][cy] == 9:
            reachable_nines.add((cx, cy))
            continue

        for dx, dy in DIRECTIONS:
            newx, newy = cx + dx, cy + dy
            if is_valid(newx, newy, rows, cols) and G[newx][newy] == G[cx][cy] + 1 not in visited:
                visited.add((newx, newy))
                stack.append((newx, newy))

    return reachable_nines

def main():
    rows = len(G)
    cols = len(G[0])
    total_score = 0

    for i in range(rows):
        for j in range(cols):
            if G[i][j] == 0:
                visited = set()
                reachable_nines = dfs(i, j, G, visited)
                total_score += len(reachable_nines)

    print(total_score)

main()