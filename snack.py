import pygame #
import time #
import random 

pygame.init()#

white = (255, 255, 255)#
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (215, 50, 80)
green = (50, 255, 0)
blue = (50, 153, 213)

dis_width=800 #зададим размер игровогополя через две переменные
dis_height=600
dis=pygame.display.set_mode((dis_width, dis_height)) #задаём размер игрового поля.
pygame.display.set_caption('Snake game by Biibars')# добовляем назвние игры 
clock = pygame.time.Clock()
snake_block = 10 #укажем величину сдвига положений змейки при нажатии на клавиши
snake_speed = 15 #укажем скорость змейки 
font_style = pygame.font.SysFont("bahnschrift", 25) #укажем название
#шрифта и его размеры для системных сообщений например, при проигрыше 
score_font = pygame.font.SysFont("comicsansms", 35)
#укажем шрифт и его размеры для отображения счёта игрока 

def your_score(score): #она будет отображать длину змейки, вычитая из неё 1
#(так как 1 это начальный размер змейки, и это не является достижением игрока)
    value = score_font.render("Ваi счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color): #создадим функцию для вывода сообщения на экран
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop(): #описываем всю игровую логику в одной функции 
    game_over = False
    game_close = False
    x1 = dis_width / 2 #указываем начальные координаты змейки по оси х
    y1 = dis_height / 2 #указываем начальные координаты змейки по оси у
    x1_change = 0 #создаем переменнуюб которой в цикле будет присваиваться значение измения координаты
    #змейки по оси х
    y1_change = 0 #создаем переменнуюб которой в цикле будет присваиваться значение измения координаты
   # змейки по оси у
    snake_List = []# создаем список для хранения координат змейки 
    length_of_snake = 1#
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#создаем перменную для хранения координаты по оси х еды
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#создаем переменную для хранения координаты по оси у еды
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("Вы проиграли! Нажмите Q - выход или С - начать заново", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:# Добовляем считывание направления движений с клавиатуры 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block #указываем шаг изменения положения змейки в snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True #Добавляем условие завершения игры при выходе за границы игрового поля
        x1 += x1_change #записываем новое значение положения змейки по оси х
        y1 += y1_change #записываем новое значение положения змейки по оси у
        dis.fill(blue)#задаём цвет фона 
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block]) 
        snake_Head = [] #создаём список, в котром будет храниться показатель длины змейки при съедении еды  
        snake_Head.append(x1) #добавляем значения в список при измении по оси х 
        snake_Head.append(y1) #добавляем значения в список при измении по оси у
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0] #удаляем первый элемент в списке длины змейки, чтобы
#она не увличивалась сама по себе при движений 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        your_score(length_of_snake - 1) #пропишем правило определения длины змейки,
#вычитая из текущей длины 1
        pygame.display.update()
        if x1 == foodx and y1 == foody: #указываем, что в случаях, 
#если координаты головы змейки совпдают с координатами еды, еда появляться в новом месте, 
#а длина змейки увеличивается на 1
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake +=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()