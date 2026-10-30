# Rato em Busca do Queijo - atividade simples com Pygame
import pygame
import random

pygame.init()

# Tamanho da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Rato em Busca do Queijo")

# Carrega as imagens
rato_img = pygame.image.load("assets/rato.png").convert_alpha()
queijo_img = pygame.image.load("assets/queijo.png").convert_alpha()

# Retângulos para posição e colisão
rato = rato_img.get_rect()
rato.topleft = (50, 50)

queijo = queijo_img.get_rect()

velocidade = 5
clock = pygame.time.Clock()


def posicionar_queijo():
    """Coloca o queijo em posição aleatória, longe do rato."""
    while True:
        queijo.x = random.randint(0, LARGURA - queijo.width)
        queijo.y = random.randint(0, ALTURA - queijo.height)
        # Evita nascer em cima do rato
        if not queijo.colliderect(rato):
            break


posicionar_queijo()

rodando = True
while rodando:
    # 1) Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2) Atualiza a posição do rato (setas)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rato.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        rato.x += velocidade
    if teclas[pygame.K_UP]:
        rato.y -= velocidade
    if teclas[pygame.K_DOWN]:
        rato.y += velocidade

    # Impede o rato de sair da janela
    if rato.left < 0:
        rato.left = 0
    if rato.right > LARGURA:
        rato.right = LARGURA
    if rato.top < 0:
        rato.top = 0
    if rato.bottom > ALTURA:
        rato.bottom = ALTURA

    # 3) Verifica colisão com o queijo
    if rato.colliderect(queijo):
        posicionar_queijo()

    # 4) Desenha os elementos
    tela.fill((200, 230, 180))  # fundo verde claro
    tela.blit(rato_img, rato)
    tela.blit(queijo_img, queijo)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
