import pygame
import sys

def game():
    bg = pygame.image.load("forest.jpg")
    bg = pygame.transform.scale(bg, (1920,1080))

    clock = pygame.time.Clock()
    FPS = 60

    y = 820
    x = 50
    pos = (x,y)


    y_enemy = 820
    x_enemy = 1880
    pos_enemy = (x_enemy,y_enemy)

    x1 = x
    y1 = y
    x2 = x
    y2 = y

    x_ded = 1000
    y_ded = 820

    Fire = False

    v = pygame.Vector2()
    v.x = x1
    v.y = y1
    k = 0

    speed = 10



    pol = pygame.Surface((1920, 700))
    pol.fill('green')

    lastMove = 'right'



    if __name__ == '__main__':
        pygame.init()
        font = pygame.font.SysFont('calibri', 24)
        text = font.render(
        'Ты уже владеешь магией огня, сын мой. Видишь того мертвеца? Покажи что ты умеешь и я дам тебе новые знания магии', 1,
            (255, 255, 255), (0, 0, 0))

        infoObject = pygame.display.Info()

        w, h = infoObject.current_w, infoObject.current_h

        screen = pygame.display.set_mode((w, h))

        screen.blit(bg, (0,-150))
        screen.blit(pol, (0, 850))

        isjump = False
        jumpCount = 10


        running = True

        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.QUIT()
            pos = (x, y)
            keys = pygame.key.get_pressed()
            mouse_key = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            if keys[pygame.K_v]:
                speed = 20
            else:
                speed = 10

            if keys[pygame.K_d] and x > 40 and x < 1880:
                x+=speed
            if keys[pygame.K_a] and x < 1880 and x > 40:
                x-=speed
            if x >= 1880:
                x-=10
            if x <= 40:
                x+=10

            if not(isjump):
                if keys[pygame.K_SPACE]:
                    isjump = True
            else:
                if jumpCount >= -10:
                    if jumpCount < 0:
                        y += (jumpCount ** 2) / 2
                    else:
                        y-=(jumpCount ** 2) / 2
                    jumpCount -= 1
                else:
                    isjump = False
                    jumpCount = 10

            pygame.display.update()
            screen.blit(bg, (0, -150))
            screen.blit(pol, (0, 850))

            pygame.draw.circle(screen, 'white', (x,y), 30)
            rect_player = pygame.Rect(x,y,30,30)

            enemy = pygame.draw.circle(screen, 'yellow', (x_enemy, y_enemy), 30)
            rect_enemy = pygame.Rect(x_enemy, y_enemy, 30, 30)

            ded = pygame.draw.circle(screen, 'pink', (x_ded, y_ded), 30)

            if x >= 1400:
                x_enemy-=1
            if x >= 900 and x <= 1000:
                screen.blit(text, (500, 750))
            if mouse_key[0]:
                x1 = mouse_pos[0]
                y1 = mouse_pos[1]
                Fire = True
            if Fire == True:
                v.x = x1 - x
                v.y = y1 - y
                x2 = int(0.1 * v.x * k) + x
                y2 = int(0.1 * v.y * k) + y
                ball = pygame.draw.circle(screen, 'red', (x2, y2), 10)
                rect_ball = pygame.Rect(x2,y2,10,10)
                if rect_ball.colliderect(rect_enemy):
                    x_enemy = -100
                pygame.time.wait(40)
                k += 1
            if k >= 10:
                k = 0
                Fire = False
                x2, y2 = x, y

            pygame.display.update()
            pygame.display.flip()
        pygame.quit()

import pygame_widgets # pip install pygame_widgets
from pygame_widgets.button import Button

fon = pygame.image.load("Back.jpg")
bg = pygame.transform.rotozoom(fon, 0, 2.8)

def terminate():
    pygame.quit()
    sys.exit(0)



if __name__ == '__main__':
    pygame.init()

    # размеры игрового экрана
    # size = w, h = 600, 600
    # screen = pygame.display.set_mode(size)

    # если хотите получить игру во весь пользовательский экран то необходимо выполнить следующие команды:
    infoObject = pygame.display.Info()
    w, h = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((w, h))

    # задаем размеры основных кнопок (в процентах относительно экрана, в примере, 20% и 10%)
    w_button, h_button = 0.2 * w, 0.1 * h

    # Создание кнопки без изображения:
    button_exit = Button(
        # обязательные параметры
        screen,  # Surface
        (w - w_button) // 2,  # X-координата левого верхнего угла
        (h - h_button) // 1.1,  # Y-координата левого верхнего угла
        w_button,  # Width
        h_button,  # Height

        # Optional Parameters
        text='Выйти из игры',  # текст на кнопке
        fontSize=50,  # размер шрифта
        margin=20,  # Минимальное расстояние между текстом/изображением и краем кнопки
        inactiveColour=(200, 50, 0),  # Цвет кнопки, когда с ней не взаимодействуют
        hoverColour=(150, 0, 0),  # Цвет кнопки при наведении курсора на нее
        pressedColour=(0, 200, 20),  # Цвет кнопки при нажатии
        radius=20,  # Радиус углов границы (оставьте пустым для не изогнутых)
        onClick=terminate # Функция, вызываемая при нажатии в этом случае закрытие игры
    )


    button_start_game = Button(
        # обязательные параметры
        screen,  # Surface
        (w - w_button) // 2,# X-координата левого верхнего угла
        h // 4.6, # Y-координата левого верхнего угла
        w_button,  # Width
        h_button,  # Height

        # Optional Parameters
        text='Новая игра',  # текст на кнопке
        fontSize=50,  # размер шрифта
        margin=20,  # Минимальное расстояние между текстом/изображением и краем кнопки
        inactiveColour=(200, 50, 0),  # Цвет кнопки, когда с ней не взаимодействуют
        hoverColour=(150, 0, 0),  # Цвет кнопки при наведении курсора на нее
        pressedColour=(0, 200, 20),  # Цвет кнопки при нажатии
        radius=20,  # Радиус углов границы (оставьте пустым для не изогнутых)
        onClick=game  # Функция, вызываемая при нажатии в этом случае открытие нового экрана
    )
    button_continue_game = Button(
        # обязательные параметры
        screen,  # Surface
        (w - w_button) // 2,  # X-координата левого верхнего угла
        h // 3,  # Y-координата левого верхнего угла
        w_button,  # Width
        h_button,  # Height

        # Optional Parameters
        text='Прождолжить',  # текст на кнопке
        fontSize=50,  # размер шрифта
        margin=20,  # Минимальное расстояние между текстом/изображением и краем кнопки
        inactiveColour=(200, 50, 0),  # Цвет кнопки, когда с ней не взаимодействуют
        hoverColour=(150, 0, 0),  # Цвет кнопки при наведении курсора на нее
        pressedColour=(0, 200, 20),  # Цвет кнопки при нажатии
        radius=20,  # Радиус углов границы (оставьте пустым для не изогнутых)
        onClick=game  # Функция, вызываемая при нажатии в этом случае открытие нового экрана
    )

    button_settings = Button(
        # обязательные параметры
        screen,  # Surface
        (w - w_button) // 2,  # X-координата левого верхнего угла
        h // 2.2,  # Y-координата левого верхнего угла
        w_button,  # Width
        h_button,  # Height

        # Optional Parameters
        text='Настройки',  # текст на кнопке
        fontSize=50,  # размер шрифта
        margin=20,  # Минимальное расстояние между текстом/изображением и краем кнопки
        inactiveColour=(200, 50, 0),  # Цвет кнопки, когда с ней не взаимодействуют
        hoverColour=(150, 0, 0),  # Цвет кнопки при наведении курсора на нее
        pressedColour=(0, 200, 20),  # Цвет кнопки при нажатии
        radius=20,  # Радиус углов границы (оставьте пустым для не изогнутых)
        onClick=game  # Функция, вызываемая при нажатии в этом случае открытие нового экрана
    )


    running = True
    all_sprite = pygame.sprite.Group()
    while running:
        screen.blit(bg,(0, 0))

        for event in pygame.event.get():
            # программа завершается, когда произошло нажатие на крестик
            if event.type == pygame.QUIT:
                running = False
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
        # button_exit.draw()
        # button_start_game.draw()
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()
    pygame.quit()