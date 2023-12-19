import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Paddle dimensions
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_COLOR = GREEN
PADDLE_SPEED = 5

# Ball dimensions
BALL_RADIUS = 10
BALL_COLOR = YELLOW
BALL_SPEED_X = random.choice([-2, 2])
BALL_SPEED_Y = 2

# Brick dimensions
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
BRICK_COLOR = BLUE

# Number of rows and columns of bricks
BRICK_ROWS = 5
BRICK_COLS = 10

# Create game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Create paddle object
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball object
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)

# Create bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + 5) + 30
        brick_y = row * (BRICK_HEIGHT + 5) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with walls
    if ball.left < 0 or ball.right > WIDTH:
        BALL_SPEED_X *= -1
    if ball.top < 0:
        BALL_SPEED_Y *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle):
        BALL_SPEED_Y *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            BALL_SPEED_Y *= -1
            break

    # Check if the ball missed the paddle
    if ball.bottom > HEIGHT:
        running = False

    # Draw background
    window.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(window, PADDLE_COLOR, paddle)

    # Draw ball
    pygame.draw.circle(window, BALL_COLOR, (ball.x, ball.y), BALL_RADIUS)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(window, BRICK_COLOR, brick)

    # Update display
    pygame.display.update()

    # Control the game's frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()