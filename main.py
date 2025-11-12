import pygame
from player import Player

# Initialize all Pygame modules
pygame.init()

# Customize game window
screen_width = 800
screen_height = 600
background = (255,255,255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("cyber-clash")

# Main game loop 
def main():
    player = Player(screen_width // 2, screen_height // 2)
    sprite = pygame.sprite.Group(player)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        sprite.update()

        screen.fill(background)
        sprite.draw(screen)
        
        # Update full display Surface to the screen
        pygame.display.flip()

main()