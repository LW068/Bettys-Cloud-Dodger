import pygame
import random

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 50

# Cloud properties
cloud_width = 100
cloud_height = 50
cloud_list = []

for i in range(5): # creates 5 clouds
    cloud_x = random.randint(0, WIDTH - cloud_width)
    cloud_y = random.randint(-500, 0)
    cloud_list.append([cloud_x, cloud_y])

cloud_speed = 8

# Set up game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloud Dodger")

# Set up font
font = pygame.font.Font(None, 64)

# Draw start button and game title
start_text = font.render("START", True, WHITE)
start_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50)
game_title = font.render("CLOUD DODGER", True, RED)
game_title_rect = game_title.get_rect(center=(WIDTH//2, HEIGHT//4))

# Set up clock
clock = pygame.time.Clock()

# Set up player
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height

# Set up game loop
menu = True
running = False
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                running = True
                menu = False

    # Draw menu screen
    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, start_button)
    start_text_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_text_rect)
    screen.blit(game_title, game_title_rect)

    pygame.display.flip()
    clock.tick(60)

# Set up cloud list
cloud_list = []
for i in range(5):
    cloud_x = random.randint(0, WIDTH - cloud_width)
    cloud_y = random.randint(-500, 0)
    cloud_list.append([cloud_x, cloud_y])

# Set up player
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height

# Start game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    player_x = max(0, min(player_x, WIDTH - player_width))

    screen.fill(WHITE)

    # Move and draw clouds
    for cloud in cloud_list:
        cloud[1] += cloud_speed
        if cloud[1] > HEIGHT:
            cloud[0] = random.randint(0, WIDTH - cloud_width)
            cloud[1] = random.randint(-500, 0)

        pygame.draw.rect(screen, BLUE, (cloud[0], cloud[1], cloud_width, cloud_height))

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
