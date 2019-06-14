import pygame
from math import ceil

def main(): 
    pygame.init()
    largura = 800
    altura = 800
    screen = pygame.display.set_mode((largura, altura))
    done = False
    is_blue = True
    t=400 # X do centro do cí,0rculo
    k=400 # Y do centro do círculo
    x = [30, 750]
    y = [391, 391]
    vel = 4
    tj = 20 # Tamanho do Jogador
    r = 14
    tb = r * 2

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        if(t - r < 0):
            t = r
        if(t + r > largura):
            t = largura - r
        if(k - r < 0):
            k = r
        if(k + r > altura):
            k = altura - r
        
        distX = abs(x[0] - x[1])
        distY = abs(y[0] - y[1])
        if(x[0] < t):
            distTX = (t - r) - (x[0] + tj)
        else:
            distTX = x[0] - (t + r)
        if(x[1] < t):
            distTX1 = (t - r) - (x[1] + tj)
        else:
           distTX1 = x[1] - (t + r)
        if(y[0] > k):
            distTY = y[0] - (k + r)
        else:
            distTY = (k - r) - (y[0] + tj) 
        if(y[1] > k):
            distTY1 = y[1] - (k + r)
        else:
            distTY1 = (k - r) - (y[1] + tj)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if(not(distX <= tj and abs(y[0] - vel - y[1]) <= tj and y[0] > y[1]) and (not(y[0] <= 0))):
                y[0] -= vel
        if pressed[pygame.K_DOWN]:
            if(not(distX <= tj and abs(y[0] + vel - y[1]) <= tj and y[0] < y[1]) and (not(y[0]+tj >= altura))):
                y[0] += vel
        if pressed[pygame.K_LEFT]:
            if(not(abs(x[0] - vel - x[1]) <= tj and distY <= tj and x[0] > x[1]) and (not(x[0] <= 0))):
                x[0] -= vel
        if pressed[pygame.K_RIGHT]:
            if(not(abs(x[0] + vel - x[1]) <= tj and distY <= tj and x[0] < x[1]) and (not(x[0] + tj >= largura))):
                x[0] += vel
        if pressed[pygame.K_w]:
            if(not(distX <= tj and abs(y[0] - (y[1] - vel)) <= tj and y[1] > y[0]) and (not(y[1] <= 0))):
                y[1] -= vel
        if pressed[pygame.K_s]:
            if(not(distX <= tj and abs(y[0] - (y[1] + vel)) <= tj and y[1] < y[0]) and (not(y[1]+tj >= altura))):
                y[1] += vel
        if pressed[pygame.K_a]:
            if(not(abs(x[0] - (x[1] - vel)) <= tj and distY <= tj and x[1] > x[0]) and (not(x[1] <= 0))):
                x[1] -= vel
        if pressed[pygame.K_d]:
            if(not(abs(x[0] - (x[1] + vel)) <= tj and distY <= tj and x[1] < x[0]) and (not(x[1]+tj >= largura))):
                x[1] += vel
        if(distTX<=0 and x[0]<t and distTY <= 0):
            t += ceil(vel)
        if(distTX<=0 and x[0]>t and distTY <= 0):
            t -= ceil(vel)
        if(distTX1<=0 and x[1]<t and distTY1 <= 0):
            t += ceil(vel)
        if(distTX1<=0 and x[1]>t and distTY1 <= 0):
            t -= ceil(vel)
        if(distTY<=0 and y[0]<k and distTX <= 0):
            k += ceil(vel)
        if(distTY<=0 and y[0]>k and distTX <= 0):
            k -= ceil(vel)
        if(distTY1 <= 0 and y[1]<k and distTX1 <= 0):
            k += ceil(vel)
        if(distTY1 <= 0 and y[1]>k and distTX1 <= 0):
            k -= ceil(vel)
        if pressed[pygame.K_g]:
            print(distTY1 == 0, y[1]<k, distTX1 <= 0)
        if pressed[pygame.K_o]:
            print("jogador 1: ", distTX, distTY, "jogador 2: ", distTX1, distTY1 , t , k)
        screen.fill((0, 0, 0))
        if is_blue:
            blue = (0, 0, 255)
            black = (0,0,0)
            orange = (255, 100, 0)
            white = (255,255,255)
            darkGreen = (0,100,0)
        pygame.draw.rect(screen,darkGreen,pygame.Rect(0,0,800,800))
        pygame.draw.circle(screen,white,[400,400],70,1)
        pygame.draw.rect(screen,white,pygame.Rect(400,0,1,800))
        pygame.draw.rect(screen,white,pygame.Rect(0,230,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(0,590,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(170,230,1,360))
        pygame.draw.rect(screen,white,pygame.Rect(630,230,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(630,590,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(630,230,1,360))
        pygame.draw.rect(screen, blue, pygame.Rect(x[0], y[0], tj, tj))
        pygame.draw.rect(screen, orange, pygame.Rect(x[1], y[1], tj, tj))
        
        pygame.draw.circle(screen, black, [t,k], r)
        
        
        pygame.display.flip()
        clock.tick(60)

main()
