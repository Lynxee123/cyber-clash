import pygame

# Initialize all Pygame modules
pygame.init()

# Customize game window
screen_width = 800
screen_height = 600
background = (255,2,255)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("cyber-clash")

# Main game loop 
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #elif 

        screen.fill(background)
        # Update full display Surface to the screen
        pygame.display.flip()

main()