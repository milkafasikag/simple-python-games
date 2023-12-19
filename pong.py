import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define game variables
FPS = 60
clock = pygame.time.Clock()

# Define paddle variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
paddle1_pos = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_pos = (HEIGHT - PADDLE_HEIGHT) // 2

# Define ball variables
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_dir = [1, 1]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1_pos > 0:
        paddle1_pos -= PADDLE_SPEED
    if keys[K_s] and paddle1_pos < HEIGHT - PADDLE_HEIGHT:
        paddle1_pos += PADDLE_SPEED
    if keys[K_UP] and paddle2_pos > 0:
        paddle2_pos -= PADDLE_SPEED
    if keys[K_DOWN] and paddle2_pos < HEIGHT - PADDLE_HEIGHT:
        paddle2_pos += PADDLE_SPEED

    # Move ball
    ball_pos[0] += BALL_SPEED_X * ball_dir[0]
    ball_pos[1] += BALL_SPEED_Y * ball_dir[1]

    # Ball collision with paddles
    if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PADDLE_HEIGHT and ball_pos[0] <= PADDLE_WIDTH:
        ball_dir[0] = 1
    if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PADDLE_HEIGHT and ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS:
        ball_dir[0] = -1

    # Ball collision with walls
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_dir[1] *= -1

    # Clear the window
    win.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(win, WHITE, (0, paddle1_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(win, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(win, WHITE, ball_pos, BALL_RADIUS)

    # Update the display
    pygame.display.update()
    clock.tick(FPS)

# Quit the game
pygame.quit()