# Import the pygame module
import pygame
import random
import sqlite3
import time
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame import USEREVENT
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_e,
    K_s,
    K_d,
    K_p,
    K_m,
    K_SPACE
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

c = sqlite3.connect('basedb.sql')
cur = c.cursor()
cur.execute('SELECT record FROM record')
recordo = cur.fetchall()
recorda = str(recordo)
recordhi = recorda.split("(")
recordwwo = str(recordhi[1])
recordwwo2 = recordwwo.split(",")
record = str(recordwwo2[0])
cur.execute('SELECT record2 FROM record2')
recordo = cur.fetchall()
recorda = str(recordo)
recordhi = recorda.split("'")
recordwwo = str(recordhi[1])
record2 = recordwwo
x = 1


# The surface drawn on the screen is now an attribute of 'player'
class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super(Gameover, self).__init__()
        self.surf = pygame.image.load("GAMEOVER.png").convert()
        self.surf.set_colorkey((255, 255, 255), )
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH - 400,
                SCREEN_HEIGHT - 270,
            )
        )

    def update(self):
        self.rect.move_ip(0, 0)
        if self.rect.right < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), )
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # Move the sprite based on speed
        # Remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def canivarvel(self, x):
        self.speed = x


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        # Move the sprite based on speed
        # Remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            Enemy.kill
        # Keep player on the screen
        if self.rect.left < 25:
            self.rect.left = 25
        if self.rect.right > SCREEN_WIDTH - 25:
            self.rect.right = SCREEN_WIDTH - 25
        if self.rect.top <= 25:
            self.rect.top = 25
        if self.rect.bottom >= SCREEN_HEIGHT - 25:
            self.rect.bottom = SCREEN_HEIGHT - 25


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.image.load("jet3.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Initialize pygame
pygame.init()
pygame.mixer.init()
# Create the screen object
clock = pygame.time.Clock()
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000, 1)
# Instantiate player. Right now, this is just a rectangle.
player = Player()
player2 = Player2()
Gameover = Gameover()
enemies = pygame.sprite.Group()
cloud = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()
all_sprites4 = pygame.sprite.Group()
all_sprites4.add(Gameover)
all_sprites.add(player)
all_sprites.add(player2)
pygame.mixer.music.load("Apoxode_-_Electric_1.ogg")
pygame.mixer.music.play(-1)
bum = pygame.mixer.Sound("Collision.ogg")
# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")
# Variable to keep the main loop running
running = True
scoreteo = 0;
time = 0
nivel = 1
vides = 4
vides2 = 4
EVENTCANVIAFONS = USEREVENT + 3
pygame.time.set_timer(EVENTCANVIAFONS, 200000)
w = 0
screen.fill((155, 155, 155))


def cargarImages():
    img = []
    img.append(pygame.image.load("GAMEOVER.png"))


def funciospeed(nivell):
    x = random.randint(nivell, nivell + 10)
    Enemy.canivarvel(Enemy, x)
    y = 5000 + (200 / nivell)
    pygame.time.set_timer(ADDENEMY, int(1000 - nivell))


# Main loop
while running:
    if w == 0:
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_p:
                    w = 1
        screen.fill((216, 191, 216))
        fuente = pygame.font.Font("8-BIT WONDER.TTF", 30)
        fuente2 = pygame.font.Font("8-BIT WONDER.TTF", 80)
        menu1 = fuente2.render("Inserteix p per inciar el vidojoc", 1, (255, 255, 255))
        menu12 = fuente2.render(("per inciar  "), 1, (255, 255, 255))
        menu13 = fuente2.render(("el vidiojoc "), 1, (255, 255, 255))
        screen.blit(menu1, (40, 35))
        screen.blit(menu12, (40, 135))
        screen.blit(menu13, (40, 235))
        pygame.display.flip()

    if w == 1:
        screen.fill((216, 191, 216))
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_s:
                    w = 3
            if event.type == KEYDOWN:
                if event.key == K_m:
                    w = 2
        fuente2 = pygame.font.Font("8-BIT WONDER.TTF", 20)
        fuente3 = pygame.font.Font("8-BIT WONDER.TTF", 50)
        menu1 = fuente2.render("Inserteix s per ", 1, (0, 255, 0))
        menu2 = fuente2.render("mode un jugador ", 1, (0, 255, 0))
        menu3 = fuente2.render("Inserteix m per ", 1, (255, 0, 0))
        menu4 = fuente2.render("mode  multijugador ", 1, (255, 0, 0))
        menu22 = fuente3.render(str(record), 1, (204, 204, 0))
        menultim = fuente3.render("RECORD", 1, (204, 204, 0))
        screen.blit(menu1, (40, 235))
        screen.blit(menu2, (40, 275))
        screen.blit(menu3, (400, 235))
        screen.blit(menu4, (400, 275))
        screen.blit(menu22, (500, 400))
        screen.blit(menultim, (150, 400))

        pygame.display.flip()

    if w == 3:

        all_sprites.remove(player2)
        screen.fill((135, 206, 250))
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                # Create the new enemy and add it to sprite groups
                new_cloud = Cloud()
                cloud.add(new_cloud)
                all_sprites.add(new_cloud)
            # Fill the screen with black

        time = time + 1
        x = len(all_sprites)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        player2.update(pressed_keys)
        temps = time / 60

        # Draw the player on the screen
        enemies.update()
        cloud.update()
        if len(all_sprites) < x:
            scoreteo = scoreteo + (10 * (x - len(all_sprites)))
        # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollide(player, enemies, True):
                # If so, then remove the player and stop the loop
                pygame.mixer.Sound.play(bum)
                player.kill()
                enemies.remove()
                if vides > 0:
                    vides = vides - 1
                    all_sprites.add(player)
                if vides2 > 0:
                    all_sprites.add(player2)
                    vides2 = vides2 - 1
            if vides == 0:
                w = 4

        fuente = pygame.font.Font("8-BIT WONDER.TTF", 20)
        fuente2 = pygame.font.Font("8-BIT WONDER.TTF", 20)
        text = "SCORE:"
        punts = text + str(scoreteo)
        mensaje = fuente2.render(str(scoreteo), 1, (173, 255, 47))
        tempo = pygame.time.get_ticks() / 1000
        tempe = round(tempo, 2)
        if scoreteo > 500:
            nivel = nivel + 1
            scoreteo = 0
        funciospeed(nivel)
        nivell = fuente2.render(str(nivel), 1, (216, 191, 216))
        screen.blit(nivell, (425, 10))
        mensaje5 = fuente2.render("Nivell", 1, (216, 191, 216))
        mensaje2 = fuente2.render("Score", 1, (173, 255, 47))
        mensaje3 = fuente2.render("Temps", 1, (255, 255, 255))
        mensaje4 = fuente2.render(str(int(tempe)), 1, (255, 255, 255))
        mensaje7 = fuente2.render(str(vides), 1, (0, 0, 0))
        screen.blit(mensaje5, (300, 10))
        screen.blit(mensaje4, (700, 10))
        screen.blit(mensaje3, (580, 10))
        screen.blit(mensaje, (120, 10))
        screen.blit(mensaje2, (15, 10))
        screen.blit(mensaje7, (400, 570))

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    if w == 2:
        screen.fill((135, 206, 250))
        if pygame.time.get_ticks() >= (20000):
            screen.fill((155, 155, 155))
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                # Create the new enemy and add it to sprite groups
                new_cloud = Cloud()
                cloud.add(new_cloud)
                all_sprites.add(new_cloud)
            # Fill the screen with black

        time = time + 1
        x = len(all_sprites)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        player2.update(pressed_keys)
        temps = time / 60

        # Draw the player on the screen
        enemies.update()
        cloud.update()
        if len(all_sprites) < x:
            scoreteo = scoreteo + (10 * (x - len(all_sprites)))
        # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollide(player, enemies, True) and vides > 0:
                # If so, then remove the player and stop the loop
                pygame.mixer.Sound.play(bum)
                player.kill()
                enemies.remove()
                if vides > 0:
                    vides = vides - 1
                    all_sprites.add(player)
                if vides == 0:
                    player.kill()
            if pygame.sprite.spritecollide(player2, enemies, True) and vides2 != 0:
                # If so, then remove the player and stop the loop
                pygame.mixer.Sound.play(bum)
                player2.kill()
                enemies.remove()
                if vides2 > 0:
                    vides2 = vides2 - 1
                    all_sprites.add(player2)
                if vides2 == 0:
                    player2.kill()
            if vides == 0 and vides2 == 0:
                x = 2
                w = 4

        fuente = pygame.font.Font(None, 20)
        fuente2 = pygame.font.Font("8-BIT WONDER.TTF", 20)
        text = "SCORE:"
        punts = text + str(scoreteo)
        mensaje = fuente2.render(str(scoreteo), 1, (173, 255, 47))
        tempo = pygame.time.get_ticks() / 1000
        tempe = round(tempo, 2)
        if scoreteo > 500:
            nivel = nivel + 1
            scoreteo = 0
        funciospeed(nivel)
        nivell = fuente2.render(str(nivel), 1, (216, 191, 216))
        screen.blit(nivell, (425, 10))
        mensaje5 = fuente2.render("Nivell", 1, (216, 191, 216))
        mensaje2 = fuente2.render("Score", 1, (173, 255, 47))
        mensaje3 = fuente2.render("Temps", 1, (255, 255, 255))
        mensaje4 = fuente2.render(str(int(tempe)), 1, (255, 255, 255))
        mensaje6 = fuente2.render(str(vides2 + 1), 1, (254, 000, 000))
        mensaje7 = fuente2.render(str(vides + 1), 1, (0, 0, 0))
        screen.blit(mensaje5, (300, 10))
        screen.blit(mensaje4, (700, 10))
        screen.blit(mensaje3, (580, 10))
        screen.blit(mensaje, (120, 10))
        screen.blit(mensaje2, (15, 10))
        screen.blit(mensaje6, (300, 570))
        screen.blit(mensaje7, (400, 570))

        # Update the display
        pygame.display.flip()
        clock.tick(60)
    if w == 4:
        screen.fill((216, 191, 216))
        fuente = pygame.font.Font("8-BIT WONDER.TTF", 70)
        nourecord = fuente.render("NOU RECORD", 1, (0, 0, 0))
        puntuacio = fuente.render(str((nivel * 500 + scoreteo) - 500), 1, (0, 0, 0) and x == 1)
        screen.blit(puntuacio, (430, 275))
        if (nivel * 500 + scoreteo - 500) > int(str(record)):
            screen.blit(nourecord, (100, 500))
            cur.executescript("DELETE FROM record;")
            score = (nivel * 500 + scoreteo - 500)
            cur.executescript("INSERT INTO record(record) Values(" + str(score) + ");")
        for entity in all_sprites4:
            screen.blit(entity.surf, entity.rect)
            pygame.display.flip()
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False
c.close  # Ensure program maintains a rate of 30 frames per sescond
pygame.mixer.music.stop()
pygame.mixer.quit()
