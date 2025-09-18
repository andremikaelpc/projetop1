import pygame
import time
import random

pygame.init()

#tela
tela_larg, tela_alt = 700, 500
tela = pygame.display.set_mode((tela_larg, tela_alt))
pygame.display.set_caption("Dinossauro")

#variáveis
distancia = 0

#coloca texto
fonte = pygame.font.SysFont("Arial", 15)
texto = fonte.render(f"DISTÂNCIA: {distancia}", True, (0, 0, 0))
texto_rect = texto.get_rect(topright=(680, 10))

#coloca sprite do dinossauro
dinossauro = pygame.image.load("imagens/dino.png.png")
dinossauro = pygame.transform.scale(dinossauro, (50, 50))

dino_rect = dinossauro.get_rect(topleft=(100, tela_alt - 200))

#chao
chao = pygame.image.load("imagens/chao.png")
chao = pygame.transform.scale(chao, (tela_larg, tela_alt))
chao_rect = chao.get_rect(topleft=(0, tela_alt - 150))

#roda o jogo
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        

    fundo = (135, 206, 235)
    tela.fill(fundo)
    tela.blit(texto, texto_rect) #posição na tela
    tela.blit(chao, chao_rect)
    tela.blit(dinossauro, dino_rect)
    pygame.display.flip()


pygame.quit()
