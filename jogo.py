import pygame
import time
import random

pygame.init()

#tela
tela_larg, tela_alt = 700, 500
tela = pygame.display.set_mode((tela_larg, tela_alt))
pygame.display.set_caption("Dinossauro")

#coloca texto
fonte = pygame.font.SysFont("Arial", 15)
distancia = fonte.render("Distância:", True, (160, 32, 240))

#coloca sprite do dinossauro
dinossauro = pygame.image.load("imagens/dino.png.png")
dinossauro = pygame.transform.scale(dinossauro, (50, 50))

dino_rect = dinossauro.get_rect(topleft=(100, tela_alt - 100))

#roda o jogo
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        

    fundo = (255, 255, 255)
    tela.fill(fundo)
    tela.blit(pontuacao, (2, 2)) #posição na tela
    tela.blit(dinossauro, dino_rect)
    pygame.display.flip()


pygame.quit()
