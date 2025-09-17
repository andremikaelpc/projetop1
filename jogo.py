import pygame
import time
import random

pygame.init()
tela_larg, tela_alt = 600, 400
tela = pygame.display.set_mode((tela_larg, tela_alt))
pygame.display.set_caption("Breakout")

fonte = pygame.font.SysFont("Calibri", 15)
pontuacao = fonte.render("PONTOS:", True, (160, 32, 240))


jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    fundo = (255, 255, 255)
    tela.fill(fundo)
    tela.blit(pontuacao, (2, 2)) #posição na tela
    pygame.display.flip()


pygame.quit()
