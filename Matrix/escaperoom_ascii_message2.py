import pygame
from random import choice, randrange
import numpy as np

#message = 'The password to this computer is "esc".'
#password_index = [2,19,36]  # "esc"
message = '"\x1bAPE" is the pAssword to this comPutEr.' # "ESCAPE" is the pAssword to this comPutEr.
password_index = [1,15,34,37]  # "escape"
binary_message = ''
binary_lst = []
binary = lambda x, n: format(x, 'b').zfill(n)
for letter in message:
    binary_message += binary(ord(letter), 8) + ' '
    binary_lst.append(binary(ord(letter), 8)+'*')
binary_message.strip()
print(binary_message)

pygame.init()

#WIDTH, HEIGHT = 1920, 1080 # full size - computer
WIDTH, HEIGHT = 1550, 800
#WIDTH, HEIGHT = 2560, 1440 # full size - screen
#WIDTH, HEIGHT = 2500, 1300
RES = (WIDTH, HEIGHT)

#FONT_SIZE = 38
FONT_SIZE = WIDTH//(len(binary_lst)+2) +1
alpha_value = 28
# the different sizes
font_1 = pygame.font.Font('ms mincho.ttf', FONT_SIZE)
font_2 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 6)
font_3 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 3)

screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(alpha_value)
pygame.display.set_caption('password in red')

clock = pygame.time.Clock()

def get_green_value(code, j):
    fonts = [font_1, font_2, font_3, font_1]
    rgb = [(randrange(0, 100), 255, randrange(0, 100)), (40, randrange(100, 175), 40), (40, randrange(50, 100), 40)]
    rgb = [(randrange(0, 100), 255, randrange(0, 100)), (40, randrange(150, 200), 40), (40, randrange(100, 175), 40), (255,0,0)]
    return [fonts[j].render(char, True, rgb[j]) for char in code]

class Symbol:
    def __init__(self, x, y, code, i):
        self.green_type = get_green_value(code, i)
        self.x = x
        self.y = y
        self.speed = 40

    def draw(self, i):
        self.value = self.green_type[i]
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))

def get_color(j):
    if j in password_index:
        return 3
    return j%3

symbols = [Symbol(FONT_SIZE * (j+1), randrange(-HEIGHT, 0), code, get_color(j)) for j, code in enumerate(binary_lst)]

run = True; i=0
while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw(i) for symbol in symbols]

    #pygame.time.delay(140)
    pygame.time.delay(100)

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    i += 1
    i %= 9