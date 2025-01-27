import pygame 
from global_constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, FPS
from grid import Grid
from input_handler import InputHandler


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pathfinding Visualizer")
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.running = True
    
    def run(self):
        """Main application loop."""
        while self.running:
            self._handle_events()
            self._update_screen()
            
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            InputHandler.handle_mouse(self.grid, event, SCREEN_WIDTH, SCREEN_HEIGHT)
            InputHandler.handle_keyboard(self.grid)

    def _update_screen(self):
        self.screen.fill(WHITE)
        self.grid.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)


if __name__ == "__main__":
    app = App()
    app.run()