import pygame
import random

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloud Dodger")

clock = pygame.time.Clock()

running = True
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height

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
