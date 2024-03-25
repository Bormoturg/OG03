import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# определение скорости движения цели
speed_x = 5
speed_y = 5

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                # при попадании изменение скорости на случайную
                speed_x = random.randint(-5, 5)
                speed_y = random.randint(-5, 5)

    # обновление позиции цели
    target_x += speed_x
    target_y += speed_y

    # проверка на выход за границы и изменение направления движения при касании границ
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        speed_x = -speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        speed_y = -speed_y

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

    # установка кадров в секунду
    clock.tick(60)

pygame.quit()
