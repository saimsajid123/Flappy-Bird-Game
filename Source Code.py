while True:
        import pygame
        from random import randint
        pygame.init()
        display=pygame.display.set_mode((320,560))
        bg=pygame.image.load("bg.png")
        bird=pygame.image.load("bird.png")
        bird_y=250
        bird_x=20
        pipe_width=70
        text=pygame.font.Font(None,30)
        pipe_gap=100
        score=0
        pipe_x=320
        bird_speed = 2
        pipe_height=randint(100,400)
        pipe_color=(0, 255, 0, 255)
        clock=pygame.time.Clock()
        while True:
            pygame.event.get()
            keys=pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                bird_y=bird_y-3-bird_speed
            if keys[pygame.K_DOWN]:
                bird_y=bird_y+6
            display.blit(bg,(0,0,))
            display.blit(bird,(bird_x,bird_y))
            pipe_x = pipe_x - 2
            if pipe_x<=-pipe_width:
                score = score + 10
                pipe_x=320
                pipe_height=randint(100,400)
            pygame.draw.rect(display,pipe_color,(pipe_x,0,pipe_width,pipe_height))
            pygame.draw.rect(display,pipe_color,(pipe_x,pipe_height+pipe_gap,pipe_width,368))
            if pipe_x<=bird_x +50 and bird_x<=pipe_x +pipe_width:

                if bird_y<=pipe_height:
                   break
                if bird_y>=pipe_height+pipe_gap:
                    break


            score_text=text.render(f"Your score:{score}",True,(255,255,255))
            display.blit(score_text,(0,0))
            bird_y = bird_y + bird_speed
            pygame.display.update()
            clock.tick(60)



