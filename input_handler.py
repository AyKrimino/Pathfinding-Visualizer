import pygame
from global_constants import CELL_SIZE


class InputHandler:
    @staticmethod
    def handle_mouse(grid, event, screen_width, screen_height):
        """
        Handles mouse clicks to set walls, start, and goal nodes.
        """
        grid_width = len(grid.grid[0]) * CELL_SIZE
        grid_height = len(grid.grid) * CELL_SIZE

        x_offset = (screen_width - grid_width) // 2
        y_offset = (screen_height - grid_height) // 2

        if event.type == pygame.MOUSEBUTTONDOWN:
            col = (event.pos[0] - x_offset) // CELL_SIZE
            row = (event.pos[1] - y_offset) // CELL_SIZE

            if not (0 <= row < len(grid.grid) and 0 <= col < len(grid.grid[0])):
                return

            mods = pygame.key.get_mods()

            if event.button == 1:  # Left click
                if mods & pygame.KMOD_CTRL:
                    if mods & pygame.KMOD_SHIFT:
                        grid.remove_node(2)
                        grid.grid[row][col] = 2
                    else:
                        grid.remove_node(1)
                        grid.grid[row][col] = 1
                else:
                    grid.grid[row][col] = 3 if grid.grid[row][col] != 3 else 0

    @staticmethod
    def handle_keyboard(grid):
        """Handles keyboard input to reset the grid."""
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()

        # Clear grid
        if keys[pygame.K_c] and mods & pygame.KMOD_CTRL:
            grid.initialize()

        # Algorithm selection
        if keys[pygame.K_1] and mods & pygame.KMOD_CTRL:  # BFS Algorithm
            grid.change_selected_algorithm(0)
        if keys[pygame.K_2] and mods & pygame.KMOD_CTRL:  # DFS Algorithm
            grid.change_selected_algorithm(1)
        if keys[pygame.K_3] and mods & pygame.KMOD_CTRL:  # A* Algorithm
            grid.change_selected_algorithm(2)

        # Run the path finding
        if keys[pygame.K_r] and mods & pygame.KMOD_CTRL: 
            if grid.is_valid():
                print("run")

