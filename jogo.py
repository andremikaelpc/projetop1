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
no_chao = True
velocidade_y = 0
gravidade = 1
piso = tela_alt - 200

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
        
        if evento.type == pygame.KEYDOWN:
            if +(evento.key == pygame.K_SPACE and no_chao) or (evento.key == pygame.K_UP and no_chao):
                no_chao = False
                velocidade_y = -20

    if not no_chao:
        dino_rect.y += velocidade_y
        velocidade_y += gravidade
        if dino_rect.y >= piso:
            dino_rect.y = piso
            no_chao = True


    fundo = (135, 206, 235)
    tela.fill(fundo)
    tela.blit(texto, texto_rect) #posição na tela
    tela.blit(chao, chao_rect)
    tela.blit(dinossauro, dino_rect)
    pygame.display.flip()


pygame.quit()
