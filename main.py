import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemy")

#Завантаження зображення
background = pygame.image.load('img/space.jpg')
player_image = pygame.image.load('img/space-ship.png')
comet_image = pygame.image.load('img/comet.png')

#Маштабування зображення
player_image = pygame.transform.scale(player_image, (60, 60))
comet_image = pygame.transform.scale(comet_image,(60, 40))


# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Швидкість оновлення екрану
clock = pygame.time.Clock()

# Гравець
player_size = 60
player_pos = [WIDTH//2, HEIGHT -2 * player_size]

# Клас для комети
class Comet:
    def __init__(self):
        self.size = random.randint(30, 50)
        self.pos = [random.randint(0, WIDTH - self.size), 0]
        self.speed = random.randint(5, 15)

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            self.pos = [random.randint(0, WIDTH - self.size), 0]
            self.speed = random.randint(5, 15)

    def draw(self):
        screen.blit(comet_image, (self.pos[0], self.pos[1]))

# Створення списку комет
comets = [Comet() for _ in range(5)]

# Функці відображення меню
def game_menu():
    menu = True
    font = pygame.font.SysFont('Monospace', 50)


    while menu:
        screen.fill(BLACK)
        lable = font.render('Space Game', 1, WHITE)
        start_lable = font.render('Start', 1, WHITE)
        quit_lable = font.render('Quit', 1, WHITE)
        screen.blit(lable, (WIDTH//2 - lable.get_width()//2, HEIGHT//4))
        screen.blit(start_lable, (WIDTH // 2 - lable.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_lable, (WIDTH // 2 - lable.get_width() // 2, HEIGHT // 1.5))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: x, y = pygame.mouse.get_pos()
            if WIDTH//2 - start_lable.get_width()//2 < x < WIDTH//2 + start_lable.get_width()//2 and HEIGHT//2 < y <HEIGHT//2 + start_lable.get_height():
                menu = False # Початок гри
            if WIDTH//2 - quit_lable.get_width()//2 < x < WIDTH//2 + quit_lable.get_width()//2 and HEIGHT//1.5 < y < HEIGHT//1.5 + quit_lable.get_height():
                pygame.quit()
                quit()
# Функція для відображення таймера

    def display_timer(start_ticks):
        font = pygame.font.SysFont('Monospace', 35)
        time_since_start = (pygame.time.get_ticks() - start_ticks) / 1000 # Час на секундах
        label = font.render(f'Timer: {time_since_start}', 1, WHITE)
        screen.bilt(label(10, 10))

# Основий цикил гри
    def game_loop():
        start_ticks = pygame.time.get_ticks() #Час початку гри
