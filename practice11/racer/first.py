import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image_background = pygame.image.load('racer/resources/AnimatedStreet.png')
image_player = pygame.image.load('racer/resources/Player.png')
image_enemy = pygame.image.load('racer/resources/Enemy.png')

#different coin images
coin_images = {
    1: pygame.transform.scale(pygame.image.load('racer/resources/dollar.png').convert_alpha(), (40, 40)),
    5: pygame.transform.scale(pygame.image.load('racer/resources/dollar.png').convert_alpha(), (50, 50)),
    10: pygame.transform.scale(pygame.image.load('racer/resources/dollar.png').convert_alpha(), (60, 60))
}

collected = 0

pygame.mixer.music.load('racer/resources/background.wav')
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound('racer/resources/crash.wav')

font = pygame.font.SysFont("Verdana", 60)
fontt = pygame.font.SysFont("Verdana", 20)

image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

score = fontt.render(f"Score: {collected}", True, "black")
score_rect = score.get_rect(center=(325, 10))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# updated Coin class with weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.weight = random.choice([1, 5, 10])  #NEW
        self.image = coin_images[self.weight]    #NEW

        self.rect = self.image.get_rect()
        self.generate_random_rect()

        self.speed = 4  #NEW (coins move)

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.top = 0  #CHANGED (spawn from top)

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()  #new (delete coin if out)


running = True
clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

#coin spawn event
COIN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_EVENT, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #spawn coins
        if event.type == COIN_EVENT:
            new_coin = Coin()
            coin_sprites.add(new_coin)
            all_sprites.add(new_coin)

    score = fontt.render(f"Score: {collected}", True, "black")

    player.move()

    screen.blit(image_background, (0, 0))
    screen.blit(score, score_rect)

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    #collect multiple coins with weight
    collected_coins = pygame.sprite.spritecollide(player, coin_sprites, True)
    for coin in collected_coins:
        collected += coin.weight

    #increase enemy speed based on score
    enemy.speed = 10 + (collected // 20)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)

        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()

        time.sleep(3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()