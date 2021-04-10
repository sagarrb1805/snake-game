import pygame
pygame.init()
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
snake_length = 10
snake_width = 10
snake_x = width/2
snake_y = height/2
velocity = 10
clock = pygame.time.Clock()


def draw_snake(snake_x, snake_y, snake_length, snake_width):
    pygame.draw.rect(screen, red, (snake_x, snake_y, snake_length, snake_width))

def snake_move():
    global snake_x, snake_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_x > 0:
        snake_x -= velocity

    if keys[pygame.K_RIGHT] and snake_x < width - snake_length:
        snake_x += velocity

    if keys[pygame.K_UP] and snake_y > 0:
        snake_y -= velocity

    if keys[pygame.K_DOWN] and snake_y < height - snake_width:
        snake_y += velocity

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    snake_move()
    draw_snake(snake_x, snake_y, snake_length, snake_width)


    pygame.display.update()
    clock.tick(10)
