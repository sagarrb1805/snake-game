import pygame
import random

pygame.init()
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

yellow = (154, 205, 50)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

game_over_font = pygame.font.Font("freesansbold.ttf", 30)
game_over_text = game_over_font.render("GAME OVER!", True, blue)

score_font = pygame.font.SysFont("timesnewroman", 20)

snake_width = 10
snake_x = width / 2
snake_y = height / 2

fruit_rad = 5

velocity_x = 0
velocity_y = 0

clock = pygame.time.Clock()

fruit_x = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
fruit_y = (random.randint(5, (width - snake_width))) / 10.0 * 10.0


def print_score(score):
    score_text = score_font.render("SCORE: {}".format(score), True, yellow)
    screen.blit(score_text, (0, 0))


def draw_fruit(x, y):
    pygame.draw.circle(screen, green, (x, y), fruit_rad)


def draw_snake(snake_size, snake_list):
    for sn in snake_list:
        pygame.draw.rect(screen, red, [sn[0], sn[1], snake_size, snake_size])


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


game_over = False

snakes = []
snake_length = 1


def main():
    global snake_x, snake_y, snake_length, snake_width, game_over, fruit_x, fruit_y, fruit_rad
    while not game_over:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_fruit(fruit_x, fruit_y)
        snake_move()

        if snake_x <= 0 or snake_x >= width:
            game_over = True
            screen.blit(game_over_text, (100, 100))

        if snake_y <= 0 or snake_y >= height:
            game_over = True
            screen.blit(game_over_text, (100, 100))

        snake_x += velocity_x
        snake_y += velocity_y

        print_score(snake_length - 1)

        draw_snake(snake_width, snakes)

        for snake in snakes[:-1]:
            if snake == [snake_x, snake_y]:
                game_over = True
                screen.blit(game_over_text, (100, 100))

        snakes.append([snake_x, snake_y])

        if fruit_x - fruit_rad < snake_x + (snake_width / 2) and fruit_x + fruit_rad > snake_x - (snake_width / 2) \
                and fruit_y - fruit_rad < snake_y + (snake_width / 2) and fruit_y + fruit_rad > snake_y - (
                snake_width / 2):
            fruit_x = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
            fruit_y = (random.randint(5, (width - snake_width))) / 10.0 * 10.0
            draw_fruit(fruit_x, fruit_y)
            snake_length += 1

        if len(snakes) > snake_length:
            del snakes[0]

        pygame.display.update()
        clock.tick(10)

    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
