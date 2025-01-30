from .constants import DIRECTIONS
from collections import deque

def is_reachable(grid, row, col):
    return row < len(grid) and row >= 0 and col < len(grid[row]) and col >= 0 and (grid[row][col] == 0 or grid[row][col] == 2) and grid[row][col] != 1

def bfs(grid, row, col):
    """Breadth-First Search yielding each visited cell for visualization."""
    queue = deque()
    queue.append((row, col))

    while queue:
        curr_row, curr_col = queue.popleft()
        yield (curr_row, curr_col)
        if grid[curr_row][curr_col] == 2:
                    return
        if grid[curr_row][curr_col] != 1:
            grid[curr_row][curr_col] = -1
        
        for dr, dc in DIRECTIONS:
            next_row, next_col = curr_row + dr, curr_col + dc
            if is_reachable(grid, next_row, next_col):
                queue.append((next_row, next_col))
