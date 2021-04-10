import pygame
import random

pygame.init()
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
# snake_length = 10
snake_width = 10
snake_x = width / 2
snake_y = height / 2
velocity_x = 0
velocity_y = 0
fruit_rad = 5

clock = pygame.time.Clock()

fruit_x = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
fruit_y = (random.randint(5, (width - snake_width))) / 10.0 * 10.0


def draw_fruit(fruit_x, fruit_y):
    pygame.draw.circle(screen, green, (fruit_x, fruit_y), fruit_rad)


def draw_snake(snake_width, snakes):
    for snake in snakes:
        pygame.draw.rect(screen, red, [snake[0], snake[1], snake_width, snake_width])


def snake_move():
    global velocity_x, velocity_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_x >= 5:
        velocity_x = -10
        velocity_y = 0

    elif keys[pygame.K_RIGHT] and snake_x < width - snake_width:
        velocity_x = 10
        velocity_y = 0

    elif keys[pygame.K_UP] and snake_y > 0:
        velocity_y = -10
        velocity_x = 0

    elif keys[pygame.K_DOWN] and snake_y < height - snake_width:
        velocity_y = 10
        velocity_x = 0


snakes = []
snake_length = 1
while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_fruit(fruit_x, fruit_y)
    snake_move()

    snake_x += velocity_x
    snake_y += velocity_y
    snakes.append([snake_x, snake_y])
    draw_snake(snake_width, snakes)

    if fruit_x - fruit_rad < snake_x + (snake_width / 2) and fruit_x + fruit_rad > snake_x - (snake_width / 2) \
            and fruit_y - fruit_rad < snake_y + (snake_width / 2) and fruit_y + fruit_rad > snake_y - (snake_width / 2):
        fruit_x = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
        fruit_y = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
        draw_fruit(fruit_x, fruit_y)
        snake_length += 1

    if len(snakes) > snake_length:
        del snakes[0]

    pygame.display.update()
    clock.tick(10)
