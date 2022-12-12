import pygame
from random import choice, randrange

message = 'The password is "xYz" followed by the value of A.'
binary_message = ''
binary = lambda x, n: format(x, 'b').zfill(n)
for letter in message:
    binary_message += binary(ord(letter), 8) + ' '
binary_message.strip()
print(binary_message)

pygame.init()

WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

FONT_SIZE = 35
alpha_value = randrange(30, 40, 5)

chars = "12345678*"

font = pygame.font.Font('ms mincho.ttf', FONT_SIZE)
font_2 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 6)
font_3 = pygame.font.Font('ms mincho.ttf', FONT_SIZE - FONT_SIZE // 3)

green_chars = [font.render(char, True, (randrange(0, 100), 255, randrange(0, 100))) for char in chars]
green_chars_2 = [font_2.render(char, True, (40, randrange(100, 175), 40)) for char in chars]
green_chars_3 = [font_3.render(char, True, (40, randrange(50, 100), 40)) for char in chars]

screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(alpha_value)

clock = pygame.time.Clock()


class Symbol:
    def __init__(self, x, y):
        self.green_type = {0:green_chars, 1:green_chars_2, 2:green_chars_3}
        self.x = x
        self.y = y
        self.speed = 40
        self.value = green_chars[0]

    def draw(self, i, j):
        self.value = self.green_type[j][i]
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))

symbols_1 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 3)]
symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 3)]

symbols = [symbols_1, symbols_2, symbols_3]
run = True; i=0
while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))
    [[symbol.draw(i,j) for symbol in symbols[j]] for j in range(3)]
    #[symbol_2.draw(i,1) for symbol_2 in symbols_2]
    #[symbol_3.draw(i,2) for symbol_3 in symbols_3]

    pygame.time.delay(100)

    pygame.display.update()

    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    i += 1
    i %= 9