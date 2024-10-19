import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уникати падіння в космосі!")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Завантаження зображень
background_image = pygame.image.load('img/space.jpg')
player_image = pygame.image.load('img/space-ship.png')
comet_image = pygame.image.load('img/comet.png')
star_image = pygame.image.load('img/star.png')  # Додали бонусний предмет (зірку)

# Масштабування зображень
player_image = pygame.transform.scale(player_image, (60, 60))
comet_image = pygame.transform.scale(comet_image, (40, 40))
star_image = pygame.transform.scale(star_image, (30, 30))

# Швидкість оновлення екрану
clock = pygame.time.Clock()

# Гравець
player_size = 60
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_lives = 3  # Додали життя гравця

# Клас для комет
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
class Star:
    def __init__(self):
        self.size = 30
        self.pos = [random.randint(0, WIDTH - self.size), 0]
        self.speed = random.randint(3, 10)

    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            self.pos = [random.randint(0, WIDTH - self.size), 0]
            self.speed = random.randint(3, 10)

    def draw(self):
        screen.blit(star_image, (self.pos[0], self.pos[1]))

# Створення списку комет і зірок
comets = [Comet() for _ in range(6)]
stars = [Star() for _ in range(3)]  # Додаємо кілька бонусних зірок

def display_stats(score, lives):
    font = pygame.font.SysFont("monospace", 35)
    score_label = font.render(f"{score}", 1, WHITE)
    lives_label = font.render(f"{lives}", 1, WHITE)
    screen.blit(score_label, (player_pos[0], player_pos[1]))
    screen.blit(lives_label, (player_pos[0], player_pos[1]))

# Функція для відображення меню
def game_menu():
    menu = True
    font = pygame.font.SysFont("monospace", 50)

    while menu:
        screen.fill(BLACK)
        label = font.render("Space Game", 1, WHITE)
        start_label = font.render("Start", 1, WHITE)
        quit_label = font.render("Quit", 1, WHITE)

        screen.blit(label, (WIDTH // 2 - label.get_width() // 2, HEIGHT // 4))
        screen.blit(start_label, (WIDTH // 2 - start_label.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_label, (WIDTH // 2 - quit_label.get_width() // 2, HEIGHT // 1.5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - start_label.get_width() // 2 < x < WIDTH // 2 + start_label.get_width() // 2 and HEIGHT // 2 < y < HEIGHT // 2 + start_label.get_height():
                    menu = False  # Почати гру
                if WIDTH // 2 - quit_label.get_width() // 2 < x < WIDTH // 2 + quit_label.get_width() // 2 and HEIGHT // 1.5 < y < HEIGHT // 1.5 + quit_label.get_height():
                    pygame.quit()
                    quit()


# Функція для відображення таймера
def display_timer(start_ticks):
    font = pygame.font.SysFont("monospace", 35)
    time_since_start = (pygame.time.get_ticks() - start_ticks) // 1000  # Час у секундах
    label = font.render(f"Time: {time_since_start}", 1, WHITE)
    screen.blit(label, (10, 10))


# Основний цикл гри
def game_loop():
    start_ticks = pygame.time.get_ticks()  # Час початку гри
    game_over = False
    score = 0
    player_lives = True

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Управління гравцем
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += 10

        # Оновлення позиції комет
        for comet in comets:
            comet.move()

        for star in stars:
            star.move()

        # Перевірка на зіткнення з кометами
        for comet in comets:
            if (player_pos[0] < comet.pos[0] + comet.size and player_pos[0] + player_size > comet.pos[0]) and \
                    (player_pos[1] < comet.pos[1] + comet.size and player_pos[1] + player_size > comet.pos[1]):
                game_over = True

        for star in stars:
            if (player_pos[0] < star.pos[0] + star.size and player_pos[0] + player_size > star.pos[0]) and \
                    (player_pos[1] < star.pos[1] + star.size and player_pos[1] + player_size > star.pos[1]):
                score += 10  # Додавання очок за збір зірок
                star.pos[1] = HEIGHT + 1  # Видалити зірку після збору

        # Очищення екрану та малювання фону
        screen.blit(background_image, (0, 0))

        # Малювання гравця
        screen.blit(player_image, (player_pos[0], player_pos[1]))

        # Малювання комет
        for comet in comets:
            comet.draw()

        for star in stars:
            star.draw()

        # Відображення таймера
        display_timer(start_ticks)

        # Оновлення екрану
        pygame.display.update()

        # Контроль кадрів
        clock.tick(60)

    pygame.quit()


# Виклик меню перед стартом гри
game_menu()

# Запуск основного циклу гри
game_loop()
