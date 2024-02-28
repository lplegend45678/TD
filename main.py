import pygame
import sys

# Definiere einige Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definiere die Bildschirmgröße
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialisiere Pygame
pygame.init()

# Erstelle den Bildschirm
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Tower Defense")

# Definiere eine einfache Klasse für den Turm
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(x, y))

# Erstelle eine Gruppe für Türme
all_towers = pygame.sprite.Group()

# Hauptspiel-Schleife
while True:
    screen.fill(WHITE)

    # Ereignisse verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Türme platzieren, wenn die linke Maustaste gedrückt wird
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tower = Tower(*event.pos)
            all_towers.add(tower)

    # Türme zeichnen
    all_towers.draw(screen)

    # Bildschirm aktualisieren
    pygame.display.flip()
