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
    piso = tela_alt - 250
    velocidade_cacto = 5
    aceleracao = 15
    contador = 0
    down = False

    #dinossauro
    dinossauro_right = pygame.image.load("imagens/dino_pe_direito.png")
    dinossauro_left = pygame.image.load("imagens/dino_pe_esquerdo.png")
    dinossauro_down_right = pygame.image.load("imagens/dino_abaixado_direito.png")
    dinossauro_down_left = pygame.image.load("imagens/dino_abaixado_esquerdo.png")
    dinossauro_right = pygame.transform.scale(dinossauro_right, (100, 150))
    dinossauro_left = pygame.transform.scale(dinossauro_left, (100, 150))
    dinossauro_down_right = pygame.transform.scale(dinossauro_down_right, (100, 150))
    dinossauro_down_left = pygame.transform.scale(dinossauro_down_left, (100, 150))
    dino_x = 100
    dino_y = tela_alt - 250

    #pterodactyl

    pterodactyl_up = pygame.image.load("imagens/pterodactyl_cima.png")
    pterodactyl_down = pygame.image.load("imagens/pterodactyl_baixo.png")
    pterodactyl_up = pygame.transform.scale(pterodactyl_up, (60, 40))
    pterodactyl_down = pygame.transform.scale(pterodactyl_down, (60, 40))
    pterodactyl_x = 700
    pterodactyl_y = tela_alt - 235

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

    #nuvens

    nuvem1 = pygame.image.load("imagens/nuvem1.png")
    nuvem1 = pygame.transform.scale(nuvem1, (50, 40))
    nuvem1_x = 500
    nuvem1_y = tela_alt - 300
    
    nuvem2 = pygame.image.load("imagens/nuvem2.png")
    nuvem2 = pygame.transform.scale(nuvem2, (50, 40))
    nuvem2_x = 650
    nuvem2_y = tela_alt - 450

    nuvem3 = pygame.image.load("imagens/nuvem3.png")
    nuvem3 = pygame.transform.scale(nuvem3, (50, 40))
    nuvem3_x = 150
    nuvem3_y = tela_alt - 375



    #criar máscaras
    mask_dino = pygame.mask.from_surface(dinossauro_right)
    mask_pterodactyl = pygame.mask.from_surface(pterodactyl_up)
    mask_cacto = pygame.mask.from_surface(cacto)

    #roda o jogo
    jogando = True
    while jogando:

        tempo = clock.tick(60) / 1000

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
                    dino_y = tela_alt - 235 
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_DOWN:
                    down = False
                    dino_y = tela_alt - 250 

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
        
        contador += 1
        if contador % 20 < 10:
            pterodactyl = pterodactyl_up
        else:
            pterodactyl = pterodactyl_down
        
        #movimento pdo pterodactyl
        pterodactyl_x -= velocidade_cacto * tempo * 50
        if pterodactyl_x < 0:
            pterodactyl_x = 700

        #if distancia % 20 < 10 and distancia >= 20:
         #   velocidade_cacto += aceleracao

        distancia += velocidade_cacto * tempo
        
        #movimento das nuvens
        nuvem1_x -= velocidade_cacto * tempo * 40
        if nuvem1_x < 0:
            nuvem1_x = 700
        
        nuvem2_x -= velocidade_cacto * tempo * 40
        if nuvem2_x < 0:
            nuvem2_x = 700
        
        nuvem3_x -= velocidade_cacto * tempo * 40
        if nuvem3_x < 0:
            nuvem3_x = 700



        #movimento dos cactos
        cacto_x -= velocidade_cacto * tempo * 80
        if cacto_x < 0:
            cacto_x = 800 + random.randint(100, 300)
        
        #colisões
        if mask_dino.overlap(mask_cacto,(cacto_x - dino_x, cacto_y - dino_y)): 
            print("bateu no cacto!")
            jogando = False
        
        if mask_dino.overlap(mask_pterodactyl,(pterodactyl_x - dino_x, pterodactyl_y - dino_y)): 
            print("bateu no pterodactyl!")
            jogando = False


        
    
        #chão
        chao_rect1.x -= 3
        chao_rect2.x -= 3

        if chao_rect1.right <= 0:
            chao_rect1.x = chao_rect2.right
        if chao_rect2.right <= 0:
            chao_rect2.x = chao_rect1.right

        #pulo
        if not floor:
            dino_y += velocidade_y * tempo * 80
            velocidade_y += gravidade * tempo * 80
            if dino_y >= piso:
                dino_y = piso
                floor = True

        texto = fonte.render(f"DISTÂNCIA: {distancia:.0f}", True, (0, 0, 0))
        texto_rect = texto.get_rect(topright=(680, 10))
    
        fundo = (100, 181, 246)
        tela.fill(fundo)
        tela.blit(texto, texto_rect) #posição na tela
        tela.blit(chao, chao_rect1)
        tela.blit(chao, chao_rect2)
        tela.blit(cacto, (cacto_x, cacto_y))
        tela.blit(nuvem1, (nuvem1_x, nuvem1_y))
        tela.blit(nuvem2, (nuvem2_x, nuvem2_y))
        tela.blit(nuvem3, (nuvem3_x, nuvem3_y))
        tela.blit(pterodactyl, (pterodactyl_x, pterodactyl_y))
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
