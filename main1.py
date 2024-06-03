import pygame
import random
pygame.init()

SCREEN_WIDHT = 800         # ширина экрана
SCREEN_HEIGHT = 600         # высота экрана
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))  # создаём окно экрана в игре

pygame.display.set_caption("Игра ТИР")      # создаём заголовок окна экрана в игре
icon = pygame.image.load("img/icon_TIR.jpg")   # загружаем в переменную icon изображение иконки игры
pygame.display.set_icon(icon)                         # устанавливаем иконку

target_img = pygame.image.load("img/target.png")      # загружаем в переменную target_img изображение цели в игре
target_widht = 80                           # ширина цели в пикселах
target_height = 80                          # высота цели в пикселах

target_x = random.randint(0, SCREEN_WIDHT - target_widht)   # задаём случайные координаты цели
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# задаём случайный цвет экрана игры
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)      # заполняем окно цветом
    for event in pygame.event.get():    # сохраняем в переменную event все события происходящие в игре
        if event.type == pygame.QUIT:  # обрабатываем событие выхода из игры (нажатие на крестик)
            running = False

# Постоянное передвижение цели/мишени + обработка выхода за границы экрана
    target_x += random.randint(-1, 1)  # изменяем координаты цели случайным образом
    target_y += random.randint(-1, 1)
    if target_x < 0:
        target_x = 0
    if target_x > SCREEN_WIDHT - target_widht:
        target_x = SCREEN_WIDHT - target_widht
    if target_y < 0:
        target_y = 0
    if target_y > SCREEN_HEIGHT - target_height:
        target_y = SCREEN_HEIGHT - target_height

    if event.type == pygame.MOUSEBUTTONDOWN:  # обрабатываем событие нажатия на кнопку мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()   # сохраняем координаты мыши
                    # проверяем попали ли мы в границы поля мишени
        if target_x < mouse_x < target_x + target_widht and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDHT - target_widht)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))    # отрисовываем цель на экране
    pygame.display.update()   # обновляем экран внутри цикла while

pygame.quit()