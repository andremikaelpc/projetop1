import pygame
import time
import random

pygame.init()

#tela
tela_larg, tela_alt = 700, 500
tela = pygame.display.set_mode((tela_larg, tela_alt))
pygame.display.set_caption("Dinossauro")
clock = pygame.time.Clock()

#texto
fonte = pygame.font.SysFont(None, 15)

def play():
    #variáveis
    distancia = 0
    no_chao = True
    velocidade_y = 0
    gravidade = 1
    piso = tela_alt - 200
    velocidade_cacto = 5

    #dinossauro
    dinossauro = pygame.image.load("imagens/dino.png.png")
    dinossauro = pygame.transform.scale(dinossauro, (50, 50))
    dino_x = 100
    dino_y = tela_alt - 200

    #chao
    chao = pygame.image.load("imagens/chao.png")
    chao = pygame.transform.scale(chao, (tela_larg, tela_alt))
    chao_rect1 = chao.get_rect(topleft=(0, tela_alt - 150))
    chao_rect2 = chao.get_rect(topleft=(700, tela_alt - 150))

    #cacto
    cacto = pygame.image.load("imagens/cacto.png")
    cacto = pygame.transform.scale(cacto, (40, 50))
    cacto_x = 700
    cacto_y = tela_alt - 200

    #criar máscaras
    mascara_dino = pygame.mask.from_surface(dinossauro)
    mascara_cacto = pygame.mask.from_surface(cacto)

    #roda o jogo
    jogando = True
    while jogando:

        tempo = clock.get_time() / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
                jogando = False
        
            if evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_SPACE and no_chao) or (evento.key == pygame.K_UP and no_chao):
                    no_chao = False
                    velocidade_y = -15

        distancia += velocidade_cacto * tempo
    
        cacto_x -= velocidade_cacto
        if cacto_x < 0:
            cacto_x = 800 + random.randint(100, 300)

        if mascara_dino.overlap(mascara_cacto,(cacto_x - dino_x, cacto_y - dino_y)):
            print("bateu no cacto!")
            jogando = False
    
        chao_rect1.x -= 3
        chao_rect2.x -= 3

        if chao_rect1.right <= 0:
            chao_rect1.x = chao_rect2.right
        if chao_rect2.right <= 0:
            chao_rect2.x = chao_rect1.right

        if not no_chao:
            dino_y += velocidade_y
            velocidade_y += gravidade
            if dino_y >= piso:
                dino_y = piso
                no_chao = True

        texto = fonte.render(f"DISTÂNCIA: {distancia:.0f}", True, (0, 0, 0))
        texto_rect = texto.get_rect(topright=(680, 10))
    
        fundo = (135, 206, 235)
        tela.fill(fundo)
        tela.blit(texto, texto_rect) #posição na tela
        tela.blit(chao, chao_rect1)
        tela.blit(chao, chao_rect2)
        tela.blit(cacto, (cacto_x, cacto_y))
        tela.blit(dinossauro, (dino_x, dino_y))
        pygame.display.flip()
        clock.tick(60)

def main():
    while True:
        play()
        esperando_reinicio = True
        pygame.display.flip()
        while esperando_reinicio:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:  # reiniciar
                        esperando_reinicio = False
        

main()
