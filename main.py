import pygame
import random
import sys
import os

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player properties and dimensions
player_width = 100
player_height = 100
player_health = 100  # Setting player health to 100%

# Hitbox adjustment for Player 
player_hitbox_offset_x = 20
player_hitbox_offset_y = 20
player_hitbox_width = player_width - player_hitbox_offset_x
player_hitbox_height = player_height - player_hitbox_offset_y

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer")

# Timer Font Size
font = pygame.font.Font(None, 22)

# Set up clock
clock = pygame.time.Clock()

# set up timer to count up
def draw_timer(screen, elapsed_time, x, y, font, color):
    timer_text = font.render(f"{int(elapsed_time // 1000)}s", True, color)
    screen.blit(timer_text, (x + 80, y))

timer_start = pygame.time.get_ticks()

def draw_health_bar(screen, health, x, y, width, height, color):
    health_percentage = max(0, min(1, health / 100))
    # Drawing health bar outline
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)
    pygame.draw.rect(
        screen,
        color,
        (x + 2,
         y + 2,
         (width - 4) * health_percentage,
            height - 4))  # Drawing health bar filled


def draw_health_percentage(screen, health, x, y, font, color):
    health_percentage_text = font.render(f"{health}%", True, color)
    screen.blit(health_percentage_text, (x, y))


# Cloud properties and dimensions
cloud_width = 100
cloud_height = 50
cloud_list = []

for i in range(5):  # creates 5 clouds
    cloud_x = random.randint(0, WIDTH - cloud_width)
    cloud_y = random.randint(-500, 0)
    cloud_list.append([cloud_x, cloud_y])

cloud_speed = 5

# Set up game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloud Dodger")
gamemenu_image = pygame.image.load('graphics/gamemenu.png')

# Set up font
font = pygame.font.Font(None, 64)
# Create a font for the health percentage
percentage_font = pygame.font.Font(None, 32)

# Draw start button and game title
start_text = font.render("START", True, WHITE)
start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
game_title = font.render("CLOUD DODGER", True, RED)
game_title_rect = game_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# Set up clock
clock = pygame.time.Clock()

# Set up player
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height

# image loader
betty_image = pygame.image.load('graphics/betty.png')
spaceimage = pygame.image.load('graphics/spaceimage.png')
space_image = pygame.image.load('graphics/spaceimage.png')
cloud_image = pygame.image.load('graphics/cloudimage.png')
cloud_image2 = pygame.image.load('graphics/cloudimage2.png')
betty_left_image = pygame.image.load('graphics/bettyleft.png')
betty_right_image = pygame.image.load('graphics/bettyright.png')
betty_image = pygame.transform.scale(betty_image, (100, 100))
betty_left_image = pygame.transform.scale(betty_left_image, (100, 100))
betty_right_image = pygame.transform.scale(betty_right_image, (100, 100))
cloud_image = pygame.transform.scale(cloud_image, (cloud_width, cloud_height))
cloud_image2 = pygame.transform.scale(cloud_image2, (cloud_width, cloud_height))

# Start CloudDodger Game Loop
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
    screen.blit(gamemenu_image, (0,0))
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

# Collisions between player and clouds
def check_collision(player, cloud):
    player_hitbox = pygame.Rect(player[0] + player_hitbox_offset_x // 2, player[1] + player_hitbox_offset_y // 2, player_hitbox_width, player_hitbox_height)
    cloud_rect = pygame.Rect(cloud[0], cloud[1], cloud_width, cloud_height)
    return player_hitbox.colliderect(cloud_rect)


# Set up game over text
game_over_text = font.render("GAME OVER", True, RED)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# Start game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += 5
        betty_image = betty_right_image

    if keys[pygame.K_LEFT]:
        player_x += -5
        betty_image = betty_left_image

    player_x = max(0, min(player_x, WIDTH - player_width))

    LIGHT_BLUE = (173, 216, 230)
    screen.fill(LIGHT_BLUE)

    elapsed_time = pygame.time.get_ticks() - timer_start
    draw_timer(screen, elapsed_time, WIDTH - 180, 10, font, RED)

    # Health Percentage Font
    percentage_font = pygame.font.Font(None, 32)

    draw_health_bar(screen, player_health, 10, 10, 200, 20, (0, 255, 0))  # Draw health bar
    draw_health_percentage(screen, player_health, 10 + 200 // 2.2 - 15, 10, percentage_font, (0, 0, 0))
    # Health bar drawn + outline

    # Move and draw clouds
    for cloud in cloud_list:
        cloud[1] += cloud_speed
        if cloud[1] > HEIGHT:
            cloud[0] = random.randint(0, WIDTH - cloud_width)
            cloud[1] = random.randint(-500, 0)

        screen.blit(cloud_image, (cloud[0], cloud[1]))
    # Choose the cloud image based on elapsed time
    if elapsed_time >= 30000:  # 30 seconds * 1000 milliseconds
        current_cloud_image = cloud_image2
    else:
        current_cloud_image = cloud_image

    screen.blit(current_cloud_image, (cloud[0], cloud[1]))

    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for cloud in cloud_list:
        cloud_rect = pygame.Rect(cloud[0], cloud[1], cloud_width, cloud_height)
        if check_collision(player_rect, cloud_rect):
            player_health -= 10  # Decrease player health by 10

    if player_health <= 0:
        running = False  # End the game if player health reaches 0% Health

    screen.blit(betty_image, (player_x, player_y))

    pygame.display.flip()
    clock.tick(60)

def game_over_screen():
    restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    restart_text = font.render("RESTART", True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return True

        screen.blit(spaceimage, (0, 0))  # game over background
        screen.blit(game_over_text, game_over_rect)
        pygame.draw.rect(screen, RED, restart_button)
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_text_rect)

        pygame.display.flip()
        clock.tick(60)

# Show the "Game Over" screen
restart = game_over_screen()

if restart:
    # If the player chose to restart, run the script again
    os.execv(sys.executable, ['python'] + sys.argv)
else:
    pygame.quit()
