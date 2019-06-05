import pygame

# Programa por Magnus e Rudigus

pygame.init()
screen = pygame.display.set_mode((620, 620))
done = False
is_blue = True
quantMinas = [10, 10]
minas = []
aux = []
for i in range(quantMinas[0]):
    for j in range(quantMinas[1]):
        aux.append(pygame.Rect(60 * i + 10, 60 * j + 10, 59, 59))
    minas.append(aux)
    aux = []
print(minas)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        posMouse = pygame.mouse.get_pos()
        print(posMouse)
       # for i in range(quantMinas[0]):
           # for j in range(quantMinas[1]):
               # if(quantMinas[i][j].x == 9999):
                  #  is_blue = not is_blue
        botoes = pygame.mouse.get_pressed()
        mouse = botoes[:1]
        if(all(mouse)):
            print("Deu certo doido da maconha")
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        for i in range(quantMinas[0]):
            for j in range(quantMinas[1]):
                pygame.draw.rect(screen, color, minas[i][j])
    pygame.display.flip()

