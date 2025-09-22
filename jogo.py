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
fonte = pygame.font.SysFont(None, 25)

def play():
    #variáveis
    distancia = 0
    floor = True
    velocidade_y = 0
    gravidade = 1
    piso = tela_alt - 200
    velocidade_cacto = 5
    contador = 0
    down = False

    #dinossauro
    dinossauro_right = pygame.image.load("imagens/dino_pe_direito.png")
    dinossauro_left = pygame.image.load("imagens/dino_pe_esquerdo.png")
    dinossauro_down_right = pygame.image.load("imagens/dino_abaixado_direito.png")
    dinossauro_down_left = pygame.image.load("imagens/dino_abaixado_esquerdo.png")
    dinossauro_right = pygame.transform.scale(dinossauro_right, (50, 60))
    dinossauro_left = pygame.transform.scale(dinossauro_left, (50, 60))
    dinossauro_down_right = pygame.transform.scale(dinossauro_down_right, (60, 40))
    dinossauro_down_left = pygame.transform.scale(dinossauro_down_left, (60, 40))
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
    mask_dino_right = pygame.mask.from_surface(dinossauro_right)
    mask_dino_left = pygame.mask.from_surface(dinossauro_left)
    mask_cacto = pygame.mask.from_surface(cacto)

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
                if (evento.key == pygame.K_SPACE and floor) or (evento.key == pygame.K_UP and floor):
                    floor = False
                    velocidade_y = -15

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN and floor:
                    down = True
                    dino_y = tela_alt - 180 
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_DOWN:
                    down = False
                    dino_y = tela_alt - 200 

        contador += 1

        if down:
            if contador % 20 < 10:
                dinossauro = dinossauro_down_right
            else:
                dinossauro = dinossauro_down_left

        else:
            if contador % 20 < 10:
                dinossauro = dinossauro_right
            else:
                dinossauro = dinossauro_left

        distancia += velocidade_cacto * tempo
    
        cacto_x -= velocidade_cacto
        if cacto_x < 0:
            cacto_x = 800 + random.randint(100, 300)

        if mask_dino_right.overlap(mask_cacto,(cacto_x - dino_x, cacto_y - dino_y)) or mask_dino_left.overlap(mask_cacto,(cacto_x - dino_x, cacto_y - dino_y)):
            print("bateu no cacto!")
            jogando = False
    
        chao_rect1.x -= 3
        chao_rect2.x -= 3

        if chao_rect1.right <= 0:
            chao_rect1.x = chao_rect2.right
        if chao_rect2.right <= 0:
            chao_rect2.x = chao_rect1.right

        if not floor:
            dino_y += velocidade_y
            velocidade_y += gravidade
            if dino_y >= piso:
                dino_y = piso
                floor = True

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
