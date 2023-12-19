import numpy as np
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("NumPy Pacman Game")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up game variables
block_size = 20
pacman_speed = 5

# Define the game grid
grid_width = width // block_size
grid_height = height // block_size
grid = np.zeros((grid_width, grid_height))

# Define the Pacman game class
class PacmanGame:
    def __init__(self):
        self.pacman = Pacman((grid_width // 2, grid_height // 2), YELLOW)
        self.ghosts = [Ghost((2, 2), BLUE), Ghost((grid_width - 3, 2), RED)]
        self.game_over = False

    def update(self):
        if not self.game_over:
            self.pacman.move()
            for ghost in self.ghosts:
                ghost.move()
            self.check_collision()

    def check_collision(self):
        pacman_x, pacman_y = self.pacman.get_position()
        for ghost in self.ghosts:
            ghost_x, ghost_y = ghost.get_position()
            if pacman_x == ghost_x and pacman_y == ghost_y:
                self.game_over = True

    def draw(self):
        screen.fill(BLACK)
        self.pacman.draw()
        for ghost in self.ghosts:
            ghost.draw()
        pygame.display.update()

# Define the Pacman class
class Pacman:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def get_position(self):
        return self.position

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position = ((self.position[0] - 1) % grid_width, self.position[1])
        elif keys[pygame.K_RIGHT]:
            self.position = ((self.position[0] + 1) % grid_width, self.position[1])
        elif keys[pygame.K_UP]:
            self.position = (self.position[0], (self.position[1] - 1) % grid_height)
        elif keys[pygame.K_DOWN]:
            self.position = (self.position[0], (self.position[1] + 1) % grid_height)

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (self.position[0] * block_size + block_size//2,
                            self.position[1] * block_size + block_size//2),
                           block_size//2)

# Define the Ghost class
class Ghost:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def get_position(self):
        return self.position

    def move(self):
        self.position = (random.choice([-1, 1]) + self.position[0], random.choice([-1, 1]) + self.position[1])
        self.position = (self.position[0] % grid_width, self.position[1] % grid_height)

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (self.position[0] * block_size + block_size//2,
                            self.position[1] * block_size + block_size//2),
                           block_size//2)

# Define the main game function
def game():
    running = True

    # Create the Pacman game object
    pacman_game = PacmanGame()

    # Game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw the game
        pacman_game.update()
        pacman_game.draw()

        # Set the game speed
        pygame.time.Clock().tick(pacman_speed)

    pygame.quit()

# Run the game
game()