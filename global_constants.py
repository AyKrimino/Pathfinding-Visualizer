# Screen properties
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GRID_ROWS = 20  
GRID_COLS = 20  
CELL_SIZE = min(SCREEN_WIDTH // GRID_COLS, SCREEN_HEIGHT // GRID_ROWS)  

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Frames per second (FPS)
FPS = 60

# Algorithms
ALGORITHMS = ("BFS", "DFS", "A*",)