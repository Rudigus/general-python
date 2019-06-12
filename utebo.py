import pygame

#Feito por Magnus e Rudigus

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
crd = [[30, 300], [600, 300]]
vel = 3.5

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue
    distX = abs(crd[0][0] - crd[1][0])
    distY = abs(crd[0][1] - crd[1][1])
    pressed = pygame.key.get_pressed()
    if(distX <= 20 and distX >= -20 and distY <= 20 and distY >= -20):
    if pressed[pygame.K_UP]: crd[0][1] -= vel
    if pressed[pygame.K_DOWN]: crd[0][1] += vel
    if pressed[pygame.K_LEFT]: crd[0][0] -= vel
    if pressed[pygame.K_RIGHT]: crd[0][0] += vel
    if pressed[pygame.K_g]: crd[1][1] -= vel
    if pressed[pygame.K_b]: crd[1][1] += vel
    if pressed[pygame.K_v]: crd[1][0] -= vel
    if pressed[pygame.K_n]: crd[1][0] += vel
    if pressed[pygame.K_o]: print(distX, distY)
    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
        color1 = (255, 100, 0)
    else:
        color = (255, 100, 0)
        color = (0, 128, 255)
    pygame.draw.rect(screen, color, pygame.Rect(crd[0][0], crd[0][1], 20, 20))
    pygame.draw.rect(screen, color1, pygame.Rect(crd[1][0], crd[1][1], 20, 20))
    pygame.display.flip()
    clock.tick(60)
