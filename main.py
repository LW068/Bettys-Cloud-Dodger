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

# Player properties and diminsions
player_width = 50
player_height = 50
player_health = 100 # Setting player health to 100%

def draw_health_bar(screen, health, x, y, width, height, color):
    health_percentage = max(0, min(1, health / 100))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)  # Drawing health bar outline
    pygame.draw.rect(screen, color, (x + 2, y + 2, (width - 4) * health_percentage, height - 4))  # Drawing health bar filled

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

# Set up font
font = pygame.font.Font(None, 64)
percentage_font = pygame.font.Font(None, 32)  # Create a font for the health percentage

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

# New function to check for collisions between player and clouds


def check_collision(player, cloud):
    return (player[0] < cloud[0] + cloud_width and
            player[0] + player_width > cloud[0] and
            player[1] < cloud[1] + cloud_height and
            player[1] + player_height > cloud[1])


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

    if keys[pygame.K_LEFT]:
        player_x += -5

    player_x = max(0, min(player_x, WIDTH - player_width))

    screen.fill(WHITE)

    percentage_font = pygame.font.Font(None, 32)  # Create a font for the health percentage

    draw_health_bar(screen, player_health, 10, 10, 200, 20, (0, 255, 0))  # Draw health bar
    draw_health_percentage(screen, player_health, 10 + 200 // 2, 10, percentage_font, (0, 255, 0))  # Draw health percentage
  
    # Move and draw clouds
    for cloud in cloud_list:
        cloud[1] += cloud_speed
        if cloud[1] > HEIGHT:
            cloud[0] = random.randint(0, WIDTH - cloud_width)
            cloud[1] = random.randint(-500, 0)

        pygame.draw.rect(
            screen,
            BLUE,
            (cloud[0],
             cloud[1],
                cloud_width,
                cloud_height))

    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for cloud in cloud_list:
        cloud_rect = pygame.Rect(cloud[0], cloud[1], cloud_width, cloud_height)
        if check_collision(player_rect, cloud_rect):
            player_health -= 10  # Decrease player health by 10

    if player_health <= 0:
        running = False  # End the game if player health reaches 0

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.draw.rect(
        screen,
        BLUE,
        (player_x,
         player_y,
         player_width,
         player_height))

    pygame.display.flip()
    clock.tick(60)

# Show the "Game Over" screen
screen.fill(WHITE)
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()
pygame.time.delay(2000)

pygame.quit()
