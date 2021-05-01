import pygame
from random import randint
import numpy as np

# Programa por Magnus e Rudigus

pygame.init()
screen = pygame.display.set_mode((620, 620))
myfont = pygame.font.SysFont("monospace", 30, 1)

done = False
is_blue = 0
quantBlocos = [10, 10]
blocos = []
minas = np.zeros((quantBlocos[0], quantBlocos[1]))
minas[:2,] = 1
minas = minas.ravel()
np.random.shuffle(minas)
minas = minas.reshape(10, 10)
aux = []
for i in range(quantBlocos[0]):
    for j in range(quantBlocos[1]):
        aux.append(pygame.Rect(60 * i + 10, 60 * j + 10, 59, 59))
    blocos.append(aux)
    aux = []
blocosAcertados = np.zeros((quantBlocos[0], quantBlocos[1]))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        posMouse = pygame.mouse.get_pos()
        for i in range(quantBlocos[0]):
            for j in range(quantBlocos[1]):
                if(blocos[i][j].collidepoint(posMouse)):
                    is_blue = (i,j)
        botoes = pygame.mouse.get_pressed()
        mouse = botoes[0]
        minaEscolhida = None
        
        if(mouse):
            minaEscolhida = minas[is_blue[0]][is_blue[1]]
            print("Deu certo doido da maconha")
            if(minaEscolhida == 1):
                print("Booooooooom")
                done = True
            else:
                blocosAcertados[is_blue[0]][is_blue[1]] = 1
                print("Ahhhh safado")
        for i in range(quantBlocos[0]):
            for j in range(quantBlocos[1]):
                if (blocosAcertados[i][j] == 1):
                    color = (0, 255, 0)
                elif not((is_blue) == (i, j)):
                    color = (0, 128, 255)
                elif (minaEscolhida == 1):
                    color = (255, 0, 0)
                else:
                    color = (255, 100, 0)
                pygame.draw.rect(screen, color, blocos[i][j])
                if (blocosAcertados[i][j] == 1):
                    label = myfont.render("5", 0, (0, 0, 0))
                    screen.blit(label, (60 * i + 30, 60 * j + 25))
        minaEscolhida = None
    pygame.display.flip()

