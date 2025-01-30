import pygame
from global_constants import (SCREEN_WIDTH, SCREEN_HEIGHT, GRID_ROWS, GRID_COLS, CELL_SIZE, WHITE, GRAY, RED, BLACK, GREEN, BLUE) 
from algorithms.dfs import dfs
from algorithms.bfs import bfs

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.selected_algorithm = 0  # Default Algorithm (BFS)
        self.start_node_indices = (-1, -1)
        self.goal_node_indices = (-1, -1)
        self.algorithms = {
            0: bfs,
            1: dfs,
        }
        
    def initialize(self):
        """Clears the grid by settings all cells to 0."""
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                self.grid[row][col] = 0
                
    def remove_node(self, value):
        """Removes a node of a specific value (1: start, 2: goal) from the grid."""
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                if self.grid[row][col] == value:
                    self.grid[row][col] = 0
                    return

    def remove_previous_path(self):
        """Removes nodes who have -1 value"""
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                if self.grid[row][col] == -1:
                    self.grid[row][col] = 0

    def change_selected_algorithm(self, index):
        """Changes the pathfinding algorithm selected by user"""
        self.selected_algorithm = index
    
    def is_valid(self):
        """Check validation for the grid (start node and goal node should be there)"""
        nbr = 0
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                if self.grid[row][col] == 1 or self.grid[row][col] == 2:
                    nbr += 1
        return nbr == 2

    def run(self):
        """Runs the selected pathfinding algorithm with animations."""
        self.remove_previous_path()
        if not self.is_valid():
            print("Invalid grid: Ensure you have both start and goal nodes.")
            return

        visited_nodes = self.algorithms[self.selected_algorithm](self.grid, *self.start_node_indices)
        for _ in visited_nodes:
            pygame.time.delay(50)
            pygame.display.get_surface().fill(WHITE)
            self.draw(pygame.display.get_surface())
            pygame.display.flip()

    def draw(self, screen):
        """Draws the grid on the screen."""
        grid_width = GRID_COLS * CELL_SIZE
        grid_height = GRID_ROWS * CELL_SIZE

        x_offset = (SCREEN_WIDTH - grid_width) // 2
        y_offset = (SCREEN_HEIGHT - grid_height) // 2

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                rect = pygame.Rect(
                    x_offset + col * CELL_SIZE,
                    y_offset + row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )

                if self.grid[row][col] == 0:
                    color = WHITE
                elif self.grid[row][col] == 1:
                    self.start_node_indices = (row, col)
                    color = GREEN
                elif self.grid[row][col] == 2:
                    self.goal_node_indices = (row, col)
                    color = RED
                elif self.grid[row][col] == 3:
                    color = BLACK
                else:
                    color = BLUE

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRAY, rect, 2)
