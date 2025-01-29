from .constants import DIRECTIONS

def is_reachable(grid, row, col):
    return row < len(grid) and row >= 0 and col < len(grid[row]) and col >= 0 and (grid[row][col] == 0 or grid[row][col] == 2)

def dfs(grid, row, col):
    """Depth-First Search yielding each visited cell for visualization."""
    if grid[row][col] == 2:
        yield (row, col)
        return True
    
    if grid[row][col] != 1:
        grid[row][col] = -1
        yield (row, col)
    
    for dr, dc in DIRECTIONS:
        next_row, next_col = row + dr, col + dc
        if is_reachable(grid, next_row, next_col):
            for step in dfs(grid, next_row, next_col):
                yield step
                if grid[step[0]][step[1]] == 2:
                    return True

    return False
