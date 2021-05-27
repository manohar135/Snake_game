import pygame, sys, random
from pygame import surface
from pygame.locals import *
from pygame.math import Vector2
import random


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (250, 0, 0), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number- 1)
        self.y = random.randint(0, cell_number- 1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(6, 10), Vector2(5, 10), Vector2(4, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 200), block_rect)

    def move_snake(self):
        if self.new_block == True:
             body_copy = self.body[:]
             body_copy.insert(0, body_copy[0] + self.direction)
             self.body = body_copy[:]
             self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class MAIN:
    def __init__(self) -> None:
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over()

        for block in self.snake.body[2:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
CLOCK = pygame.time.Clock()

cell_size = 20
cell_number = 40
SCREEN_WIDTH = 800
SCREEN_HIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    main_game.draw_elements()
    CLOCK.tick(60)
    pygame.display.update()