import pygame
from player import Player
pygame.init()

# Set up display
screen = pygame.display.set_mode((2000, 1500))
pygame.display.set_caption("Tron Game")

# Create players
player1 = Player(100, 100, (255, 0, 0))
player2 = Player(700, 500, (0, 0, 255))

# List to store player trails
player1_trail = []
player2_trail = []

# Example of drawing a trail
def draw_trail(trail, player):
    for segment in trail:
        pygame.draw.rect(screen, player.color, (*segment, 5, 5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
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

     # Update game state here
    player1.move()
    player2.move()

    # Append the current position to the trail
    player1Pos = (player1.x,player1.y)
    player2Pos = (player2.x,player2.y)
    
   

    # Draw players, trails, etc.

    #checking for collisions
    if player1Pos in player1_trail:
        print("Blue is Winner")
        break
    if player1Pos in player2_trail:
        print("Blue is Winner")
        break
    if player2Pos in player1_trail:
        print("Red is Winner")
        break
    if player2Pos in player2_trail:
        print("Red is Winner")
        break

    player1_trail.append((player1.x, player1.y))
    player2_trail.append((player2.x, player2.y))

    # resets screen to black
    screen.fill((0, 0, 0))
    # Drawing 
    draw_trail(player1_trail, player1)
    draw_trail(player2_trail, player2)
    pygame.draw.rect(screen, player1.color, (player1.x, player1.y, 10, 10))
    pygame.draw.rect(screen, player2.color, (player2.x, player2.y, 10, 10))
    
    pygame.display.update()