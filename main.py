import pygame
import sys
from player import Player

pygame.init()

# Set up display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Tron Game")

# Create players
player1 = Player(300, 300, (255, 0, 0))
player2 = Player(300, 500, (0, 0, 255))

# List to store player trails
player1_trail = []
player2_trail = []


# Example of drawing a trail
def draw_trail(trail, player):
    for segment in trail:
        pygame.draw.rect(screen, player.color, (*segment, 5, 5))


def clear_trail(trail):
    for segment in trail:
        pygame.draw.rect(screen, (0, 0, 0), (*segment, 5, 5))


# Define GUI elements
font = pygame.font.Font(None, 36)

# Create buttons
start_button = pygame.Rect(100, 100, 150, 50)
reset_button = pygame.Rect(100, 200, 150, 50)

# Define button colors
start_color = (0, 255, 0)
reset_color = (255, 0, 0)

# Define button texts
start_text = font.render("Start", True, (255, 255, 255))
reset_text = font.render("Reset", True, (255, 255, 255))

# Variables for game state
game_running = False
game_paused = False

# Handling user events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_running and not game_paused:
            if event.type == pygame.KEYDOWN:
                # Handle player movements when the game is running
                if event.key == pygame.K_w:
                    player1.change_direction("UP")
                elif event.key == pygame.K_s:
                    player1.change_direction("DOWN")
                elif event.key == pygame.K_a:
                    player1.change_direction("LEFT")
                elif event.key == pygame.K_d:
                    player1.change_direction("RIGHT")

                if event.key == pygame.K_UP:
                    player2.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    player2.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    player2.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    player2.change_direction("RIGHT")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print("Start Button Pressed")
                game_running = True
                game_paused = False

            if reset_button.collidepoint(event.pos):
                print("Reset Button Pressed")
                clear_trail(player1_trail)
                clear_trail(player2_trail)
                player1_trail = []
                player2_trail = []
                player1.x, player1.y = 300, 300
                player2.x, player2.y = 300, 500
                game_running = False
                game_paused = True

    if game_running and not game_paused:
        # Update game state here
        player1.move()
        player2.move()

        player1_pos = (player1.x, player1.y)
        player2_pos = (player2.x, player2.y)

        # Checking for collisions
        if player1_pos in player1_trail or player1_pos in player2_trail:
            print("Blue is Winner")
            game_paused = True

        if player2_pos in player1_trail or player2_pos in player2_trail:
            print("Red is Winner")
            game_paused = True

        player1_trail.append((player1.x, player1.y))
        player2_trail.append((player2.x, player2.y))

        # Resets screen to black
        screen.fill((0, 0, 0))

        # Drawing
        draw_trail(player1_trail, player1)
        draw_trail(player2_trail, player2)

        pygame.draw.rect(screen, player1.color, (player1.x, player1.y, 10, 10))
        pygame.draw.rect(screen, player2.color, (player2.x, player2.y, 10, 10))

    # Draw buttons on the screen
    pygame.draw.rect(screen, start_color, start_button)
    pygame.draw.rect(screen, reset_color, reset_button)
    screen.blit(start_text, (115, 115))
    screen.blit(reset_text, (115, 215))

    # Screen refresh
    pygame.display.update()
