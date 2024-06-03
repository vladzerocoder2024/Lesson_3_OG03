import pygame

pygame.init()

SCREEN_WIDHT = 800         # ширина экрана
SCREEN_HIGHT = 600         # высота экрана
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))  # создаём окно экрана в игре

pygame.display.set_caption("Игра ТИР")      # создаём заголовок окна экрана в игре
icon = pygame.image.load("")                # загружаем в переменную icon изображение иконки игры


running = True
while running:
    pass

pygame.quit()

