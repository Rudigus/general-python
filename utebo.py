import pygame

def main(): 
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    is_blue = True
    x = [30, 600]
    y = [300, 300]
    vel = 3.5
    tj = 20 # Tamanho do Jogador

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        distX = abs(x[0] - x[1])
        distY = abs(y[0] - y[1])
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if(not(distX <= tj and abs(y[0] - vel - y[1]) <= tj and y[0] > y[1])):
                y[0] -= vel
        if pressed[pygame.K_DOWN]:
            if(not(distX <= tj and abs(y[0] + vel - y[1]) <= tj and y[0] < y[1])):
                y[0] += vel
        if pressed[pygame.K_LEFT]:
            if(not(abs(x[0] - vel - x[1]) <= tj and distY <= tj and x[0] > x[1])):
                x[0] -= vel
        if pressed[pygame.K_RIGHT]:
            if(not(abs(x[0] + vel - x[1]) <= tj and distY <= tj and x[0] < x[1])):
                x[0] += vel
        if pressed[pygame.K_w]:
            if(not(distX <= tj and abs(y[0] - (y[1] - vel)) <= tj and y[1] > y[0])):
                y[1] -= vel
        if pressed[pygame.K_s]:
            if(not(distX <= tj and abs(y[0] - (y[1] + vel)) <= tj and y[1] < y[0])):
                y[1] += vel
        if pressed[pygame.K_a]:
            if(not(abs(x[0] - (x[1] - vel)) <= tj and distY <= tj and x[1] > x[0])):
                x[1] -= vel
        if pressed[pygame.K_d]:
            if(not(abs(x[0] - (x[1] + vel)) <= tj and distY <= tj and x[1] < x[0])):
                x[1] += vel
        if pressed[pygame.K_o]:
            print(distX, distY)
        screen.fill((0, 0, 0))
        if is_blue:
            color = (0, 128, 255)
            color1 = (255, 100, 0)
        else:
            color = (255, 100, 0)
            color = (0, 128, 255)
        pygame.draw.rect(screen, color, pygame.Rect(x[0], y[0], tj, tj))
        pygame.draw.rect(screen, color1, pygame.Rect(x[1], y[1], tj, tj))
        pygame.display.flip()
        clock.tick(60)

main()
