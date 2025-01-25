import pygame
from global_constants import (SCREEN_WIDTH, SCREEN_HEIGHT, GRID_ROWS, GRID_COLS, CELL_SIZE, WHITE, GRAY, FPS)


def draw_grid(screen):
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
            pygame.draw.rect(screen, GRAY, rect, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_grid(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()