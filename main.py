import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Enemy")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Швидкість оновлення екрану
clock = pygame.time.Clock()

# Гравець
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Ворог (блок, що падає)
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -enemy_size
enemy_speed = 5

# Функція для відображення гравця
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

# Функція для відображення ворога
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

# Головний цикл гри
running = True
while running:
    clock.tick(60)  # 60 кадрів на секунду
    screen.fill(BLACK)  # Очищення екрану

    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управління гравцем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Падіння ворога
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # Перевірка зіткнення
    if (enemy_y + enemy_size > player_y and
        enemy_x < player_x + player_size and
        enemy_x + enemy_size > player_x):
        running = False  # Гра закінчується при зіткненні

    # Відображення гравця та ворога
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)

    # Оновлення екрану
    pygame.display.flip()

pygame.quit()
