import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up game variables
snake_size = 20
snake_speed = 10

# Define the snake class
class Snake:
    directions = {
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1),
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0)
    }

    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice(list(self.directions.values()))
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction

        new = (((cur[0] + (x * snake_size)) % width), (cur[1] + (y * snake_size)) % height)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice(list(self.directions.values()))

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], snake_size, snake_size))

    def handle_keys(self, keys):
        for key in self.directions:
            if keys[key]:
                self.direction = self.directions[key]

# Define the main game function
def game():
    running = True

    # Create the snake object
    snake = Snake()

    # Generate food position
    food_pos = (random.randint(0, width // snake_size - 1) * snake_size,
                random.randint(0, height // snake_size - 1) * snake_size)

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the keys pressed
        keys = pygame.key.get_pressed()

        # Move the snake
        snake.handle_keys(keys)
        snake.move()

        # Check if snake eats food
        if snake.get_head_position() == food_pos:
            snake.length += 1
            food_pos = (random.randint(0, width // snake_size - 1) * snake_size,
                        random.randint(0, height // snake_size - 1) * snake_size)

        # Draw on the screen
        screen.fill(BLACK)
        snake.draw(screen)
        pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], snake_size, snake_size))
        pygame.display.update()

        # Set the snake speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

# Run the game
game()