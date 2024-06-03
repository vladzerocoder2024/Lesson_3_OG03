import pygame
import random
pygame.init()

SCREEN_WIDHT = 800         # ширина экрана
SCREEN_HIGHT = 600         # высота экрана
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HIGHT))  # создаём окно экрана в игре

pygame.display.set_caption("Игра ТИР")      # создаём заголовок окна экрана в игре
<<<<<<< Updated upstream
icon = pygame.image.load("img/Иконка игры ТИР.jpg")   # загружаем в переменную icon изображение иконки игры
pygame.display.set_icon(icon)                         # устанавливаем иконку

target_img = pygame.image.load("img/мишень.png")      # загружаем в переменную target_img изображение цели в игре
target_wight = 50                           # ширина цели в пикселах
target_height = 50                          # высота цели в пикселах

targer_x = random.randint(0, SCREEN_WIDHT - target_wight)   # задаём случайные координаты цели
targer_y = random.randint(0, SCREEN_HIGHT - target_height)

Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    # задаём случайный цвет экрана игры

=======
icon = pygame.image.load("img/")                # загружаем в переменную icon изображение иконки игры
>>>>>>> Stashed changes


running = True
while running:
    pass

pygame.quit()

# Что то пошло не так. 