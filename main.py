# Import and initialize the pygame library
import pygame
pygame.init()
screen_width = 800
screen_height = 500
box_width = 100
box_height = 100
player_x = 0
player_y = 0
vel_x = 0.2
vel_y = 0.2

# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_x += vel_x
    if keys[pygame.K_a]:
        player_x -= vel_x
    if keys[pygame.K_w]:
        player_y -= vel_y
    if keys[pygame.K_s]:
        player_y += vel_y

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x - box_width / 2, player_y - box_height / 2,
                                           box_width, box_height))
    if keys[pygame.K_SPACE]:
        pygame.draw.circle(screen, (44, 55, 66), (player_x, player_y), 10, 0)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

