import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (50, 153, 213)
light_blue = (173, 216, 230)

# Параметры дисплея
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка от Biibars")

# Параметры игры
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счёта
def your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [10, 10])

# Отрисовка змейки
def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])

# Сообщения на экране
def message(msg, color, x_offset=0, y_offset=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6 + x_offset, dis_height / 3 + y_offset])

# Основная логика игры
def gameLoop():
    game_over = False
    game_close = False

    # Начальное положение змейки
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    # Параметры змейки
    snake_List = []
    length_of_snake = 1

    # Координаты еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            dis.fill(light_blue)
            message("Вы проиграли!", red, y_offset=-50)
            message("Q - выход, C - начать заново", black, y_offset=50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка выхода за границы поля
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(light_blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Управление длиной змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        # Проверка столкновения с самим собой
        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Проверка съедания еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
# 1. Ошибка в границах игрового поля для еды
# В вашем коде координаты еды рассчитывались как:

# python
# Копировать код
# foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
# Однако вы использовали 10.0 для деления и округления, несмотря на то, что размер блока змейки (snake_block) был установлен в 20. Это могло привести к тому, что еда появлялась не на кратных позициях, несовместимых с размером змейки.

# Исправлено на:

# python
# Копировать код
# foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
# 2. Ошибка с движением змейки в противоположную сторону
# Вы не учитывали, что змейка не может двигаться сразу в противоположном направлении (например, слева направо сразу же налево). Это приводило к столкновению и завершению игры.

# Исправлено: Добавлены условия, предотвращающие изменение направления на противоположное:

# python
# Копировать код
# if event.key == pygame.K_LEFT and x1_change == 0:
#     x1_change = -snake_block
#     y1_change = 0
# elif event.key == pygame.K_RIGHT and x1_change == 0:
#     x1_change = snake_block
#     y1_change = 0
# elif event.key == pygame.K_UP and y1_change == 0:
#     y1_change = -snake_block
#     x1_change = 0
# elif event.key == pygame.K_DOWN and y1_change == 0:
#     y1_change = snake_block
#     x1_change = 0
# 3. Проблема с пересечением змейки
# В случае, если змейка пересекала саму себя, игра не всегда правильно завершалась. Это могло произойти из-за проверки только последнего элемента списка.

# Исправлено: Теперь проверка проходит по всему телу змейки (кроме головы):

# python
# Копировать код
# for block in snake_List[:-1]:
#     if block == snake_Head:
#         game_close = True
# 4. Неправильный порядок логики при обновлении змейки
# В вашем коде вы удаляли элементы из списка змейки, но могли делать это до завершения всех проверок, что иногда приводило к несогласованности.

# Исправлено: Логика управления длиной змейки чётко отделена от других функций.

# 5. Визуальные аспекты
# Фон был белым, что не всегда приятно для глаз.
# Змейка и еда имели цвета, которые плохо сочетались с фоном.
# Добавлено больше эстетики: светло-голубой фон, яркая зелёная еда, чёрная змейка.
# 6. Система сообщений
# Сообщение о проигрыше было трудно читаемым. Теперь оно выделено красным цветом с пояснением действий.
# 7. Простые улучшения кода
# Добавлены комментарии, поясняющие ключевые моменты.
# Упрощён вывод счёта, а шрифт сделан более заметным.
# Общая структура игры стала чище и понятнее.
