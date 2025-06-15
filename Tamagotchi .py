# Tamagotchi
# Criador: Leonardo de Moura Fuseti
# Email: mourafuseti@hotmail.com

import asyncio
import platform
import pygame
import math
import random

# Configurações
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
FONT_SIZE = 20
TITLE_FONT_SIZE = 30

# Inicialização
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamagotchi")
font = pygame.font.SysFont('arial', FONT_SIZE)
title_font = pygame.font.SysFont('arial', TITLE_FONT_SIZE, bold=True)
clock = pygame.time.Clock()

# Estado do Tamagotchi
hunger = 100
happiness = 100
health = 100
is_alive = True
blink_timer = 0
blink_state = True  # True = olhos abertos, False = olhos fechados
update_timer = 0  # Para atualizar atributos

# Botões
buttons = [
    {"text": "Alimentar", "rect": pygame.Rect(300, 450, 100, 40), "color": GREEN, "hover_color": (100, 255, 100), "action": "feed"},
    {"text": "Brincar", "rect": pygame.Rect(450, 450, 100, 40), "color": BLUE, "hover_color": (100, 100, 255), "action": "play"},
    {"text": "Curar", "rect": pygame.Rect(600, 450, 100, 40), "color": RED, "hover_color": (255, 100, 100), "action": "heal"}
]
button_texts = [font.render(btn["text"], True, WHITE) for btn in buttons]

def draw_tamagotchi():
    center = (400, 300)
    radius = 160  # Aumentado de 80 para 160 (2x maior)
    # Corpo
    pygame.draw.circle(screen, (255, 200, 200), center, radius)
    # Expressão baseada nos atributos
    if health <= 0:
        # Morto
        pygame.draw.line(screen, BLACK, (center[0] - 64, center[1] - 64), (center[0] - 32, center[1] - 32), 5)
        pygame.draw.line(screen, BLACK, (center[0] - 64, center[1] - 32), (center[0] - 32, center[1] - 64), 5)
        pygame.draw.line(screen, BLACK, (center[0] + 32, center[1] - 64), (center[0] + 64, center[1] - 32), 5)
        pygame.draw.line(screen, BLACK, (center[0] + 32, center[1] - 32), (center[0] + 64, center[1] - 64), 5)
        pygame.draw.arc(screen, BLACK, (center[0] - 64, center[1], 128, 64), math.radians(0), math.radians(180), 5)
    elif health < 30 or hunger < 30 or happiness < 30:
        # Triste/doente
        if blink_state:
            pygame.draw.circle(screen, BLACK, (center[0] - 64, center[1] - 64), 16)  # Olhos 2x maiores
            pygame.draw.circle(screen, BLACK, (center[0] + 64, center[1] - 64), 16)
        pygame.draw.arc(screen, BLACK, (center[0] - 64, center[1], 128, 64), math.radians(0), math.radians(180), 5)
    else:
        # Feliz
        if blink_state:
            pygame.draw.circle(screen, BLACK, (center[0] - 64, center[1] - 64), 16)  # Olhos 2x maiores
            pygame.draw.circle(screen, BLACK, (center[0] + 64, center[1] - 64), 16)
        pygame.draw.arc(screen, BLACK, (center[0] - 64, center[1] - 32, 128, 64), math.radians(180), math.radians(360), 5)

def draw_bars():
    # Barras de atributos
    pygame.draw.rect(screen, GRAY, (50, 100, 200, 20))  # Fome fundo
    pygame.draw.rect(screen, GREEN, (50, 100, hunger * 2, 20))  # Fome
    pygame.draw.rect(screen, GRAY, (50, 140, 200, 20))  # Felicidade fundo
    pygame.draw.rect(screen, BLUE, (50, 140, happiness * 2, 20))  # Felicidade
    pygame.draw.rect(screen, GRAY, (50, 180, 200, 20))  # Saúde fundo
    pygame.draw.rect(screen, RED, (50, 180, health * 2, 20))  # Saúde
    # Textos
    hunger_text = font.render(f"Fome: {int(hunger)}", True, BLACK)
    happiness_text = font.render(f"Felicidade: {int(happiness)}", True, BLACK)
    health_text = font.render(f"Saúde: {int(health)}", True, BLACK)
    screen.blit(hunger_text, (50, 70))
    screen.blit(happiness_text, (50, 110))
    screen.blit(health_text, (50, 150))

def setup():
    global hunger, happiness, health, is_alive, blink_timer, update_timer
    hunger = 100
    happiness = 100
    health = 100
    is_alive = True
    blink_timer = 0
    update_timer = 0

def update_loop():
    global hunger, happiness, health, is_alive, blink_timer, update_timer, blink_state
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        if event.type == pygame.MOUSEBUTTONDOWN and is_alive:
            for btn in buttons:
                if btn["rect"].collidepoint(event.pos):
                    if btn["action"] == "feed":
                        hunger = min(hunger + 20, 100)
                    elif btn["action"] == "play":
                        happiness = min(happiness + 15, 100)
                    elif btn["action"] == "heal":
                        health = min(health + 25, 100)
    screen.fill(WHITE)
    # Título
    title_text = title_font.render("Tamagotchi", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
    if is_alive:
        # Atualizar atributos
        update_timer += 1 / FPS
        if update_timer >= 10:  # A cada 10 segundos
            hunger = max(hunger - 5, 0)
            happiness = max(happiness - 3, 0)
            if hunger < 30 or happiness < 30:
                health = max(health - 2, 0)
            update_timer = 0
        # Atualizar animação de piscar
        blink_timer += 1 / FPS
        if blink_timer >= 2:
            blink_state = not blink_state
            blink_timer = 0
        # Desenhar elementos
        draw_tamagotchi()
        draw_bars()
        # Botões
        for btn, btn_text in zip(buttons, button_texts):
            btn_color = btn["hover_color"] if btn["rect"].collidepoint(mouse_pos) else btn["color"]
            pygame.draw.rect(screen, btn_color, btn["rect"], border_radius=10)
            screen.blit(btn_text, (btn["rect"].x + (btn["rect"].width - btn_text.get_width()) // 2, btn["rect"].y + 10))
        if health <= 0:
            is_alive = False
    else:
        # Game Over
        game_over_text = title_font.render("Game Over: Seu Tamagotchi morreu!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())