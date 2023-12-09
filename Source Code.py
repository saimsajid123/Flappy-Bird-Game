import pygame
from pygame.locals import *
from random import randint

pygame.init()

# Set up display
display = pygame.display.set_mode((320, 560))
pygame.display.set_caption("Flappy Bird")

# Load images and fonts
bg = pygame.image.load("background.png")
bird = pygame.image.load("bird.png")
start_image = pygame.image.load("start_screen.png")
text_font = pygame.font.Font(None, 30)

# Load background music
pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Bird and pipe variables
bird_y = 250
bird_x = 20
pipe_width = 70
pipe_gap = 100
score = 0
pipe_x = 320
bird_speed = 2
pipe_height = randint(100, 400)
pipe_color = (0, 255, 0, 255)
clock = pygame.time.Clock()

# Display start screen
display.blit(start_image, (0, 0))
pygame.display.update()

# Wait for user input to start the game
start = False
while not start:
    for event in pygame.event.get():
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
            start = True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bird_y = bird_y - 3 - bird_speed
        if keys[pygame.K_DOWN]:
            bird_y = bird_y + 6

    display.blit(bg, (0, 0))
    display.blit(bird, (bird_x, bird_y))
    pipe_x = pipe_x - 2
    if pipe_x <= -pipe_width:
        score = score + 10
        pipe_x = 320
        pipe_height = randint(100, 400)

    pygame.draw.rect(display, pipe_color, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(display, pipe_color, (pipe_x, pipe_height + pipe_gap, pipe_width, 368))

    if pipe_x <= bird_x + 50 and bird_x <= pipe_x + pipe_width:
        if bird_y <= pipe_height or bird_y >= pipe_height + pipe_gap:
            end_text = text_font.render(f"Your final score: {score}", True, (255, 255, 255))
            display.blit(end_text, (50, 200))
            exit_restart_text = text_font.render("Press 'E' to exit or 'R' to restart", True, (255, 255, 255))
            display.blit(exit_restart_text, (20, 250))
            pygame.display.update()

            end = False
            while not end:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            running = False
                            end = True
                        elif event.key == pygame.K_r:
                            bird_y = 250
                            bird_x = 20
                            pipe_x = 320
                            score = 0
                            end = True

    score_text = text_font.render(f"Your score: {score}", True, (255, 255, 255))
    display.blit(score_text, (0, 0))
    bird_y = bird_y + bird_speed
    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
