import os
import random

import pygame

pygame.mixer.init()

pygame.init()

# colors
green = (0, 100, 0)
lightgreen = (144, 238, 144)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (1, 1, 1)
skyblue = (135, 206, 250)
yellow = (255, 255, 204)
brown = (178, 34, 34)
# game vaariables
font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
pygame.display.set_mode((screen_width,screen_height))
bgimg = pygame.image.load("back2.jpg")
bgimg = pygame.transform.scale(
    bgimg, (screen_width, screen_height)).convert_alpha()
# bgimg1 = pygame.image.load("back1.jpg")
# bgimg1 = pygame.transform.scale(
#     bgimg1, (screen_width, screen_height)).convert_alpha()
# game display
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game By Nilesh")
pygame.display.update()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, green, [
            x, y, snake_size, snake_size])


def welcome():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('back.mp3'))
    exit_game = False
    while not exit_game:
        #welcome screen
        gameWindow.fill(skyblue)
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Welcome to Snakes", green,
                    screen_width/4, screen_height/3)
        text_screen("Created by Nilesh Malav", blue,
                    screen_width/5, screen_height/2.4)
        text_screen("Press SpaceBar to Play", brown,
                    screen_width/4.8, screen_height/2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    gameLoop()
        pygame.display.update()
        clock.tick(60)
# game loop


def gameLoop():  # game Variables
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('back3.mp3'))
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    init_velocity = 5
    velocity_x = 5
    velocity_y = 0
    food_x = random.randint(10, screen_width-10)
    food_y = random.randint(10, screen_height-10)
    score = 0
    snake_size = 15
    fps = 60
    if (not os.path.exists("high score.txt")):
        with open("high score.txt", "w") as f:
            f.write("0")
    with open("high score.txt", "r") as f:
        high_score = f.read()
    while not exit_game:
        if game_over:
#game over screen
            gameWindow.fill(lightgreen)
            gameWindow.blit(bgimg, (0, 0))
            with open("high score.txt", "w") as f:
                f.write(str(high_score))
            text_screen("Game Over!",
                        red, screen_width/3, screen_height/2.4)
            text_screen("Press ENTER to Continue",
                        blue, screen_width/6, screen_height/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x = + init_velocity
                        velocity_y = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            velocity_x = - init_velocity
                            velocity_y = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            velocity_y = - init_velocity
                            velocity_x = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            velocity_y = + init_velocity
                            velocity_x = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            score = score+10
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x-food_x) < 14 and abs(snake_y-food_y) < 14:
                score = score+10
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('beep.mp3'))
                food_x = random.randint(10, screen_width-10)
                food_y = random.randint(10, screen_height-10)
                snk_length += 5
                if score > int(high_score):
                    high_score = score
            #game screen
            gameWindow.fill(yellow)
            text_screen("score: "+str(score) + "    high Score: " +
                        str(high_score), blue, 5, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
                pygame.draw.rect(gameWindow, red, [
                    food_x, food_y, snake_size, snake_size])
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('over2.mp3'))

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('over2.mp3'))
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


welcome()
pygame.quit()
quit()
