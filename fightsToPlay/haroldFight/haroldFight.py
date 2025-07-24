"""
Following the trend, this will be a minigame, will have to make a victory/defeat
"""
"""this one will be space invaders of a sort"""
import pygame
import random
import math
from time import *

# pygame setup
pygame.init()
pygame.mixer.init()

# Game attributes
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 900
PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
# --- NEW: Define the size of the actual hitbox ---
# It's much smaller for easier dodging. Feel free to adjust these!
PLAYER_HITBOX_WIDTH = PLAYER_WIDTH // 3
PLAYER_HITBOX_HEIGHT = PLAYER_HEIGHT // 3

PLAYER_MAX_HEALTH = 100
PLAYER_SPEED = 5
player_health = PLAYER_MAX_HEALTH

BULLET_WIDTH, BULLET_HEIGHT = 50, 100
PLAYER_BULLET_SPEED = 10 # Player bullets are faster
ENEMY_BULLET_SPEED = 6 # Speed for enemy bullets
BULLET_DAMAGE = 10
PLAYER_FIRE_PAUSE = 30

ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT = 110, 110
ENEMY_SPEED = 5  # Increased enemy mobility
ENEMY_FIRE_PAUSE = 70  # Cooldown for regular shots
ENEMY_SPECIAL_ATTACK_COOLDOWN = 180 # Cooldown for the 8-bullet special attack
ENEMY_MAX_HEALTH = 200
enemy_health = ENEMY_MAX_HEALTH

SCORE_FONT_SIZE = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_over = False
victory = False
clock = pygame.time.Clock()
running = True

# Load images
player_ship_image = pygame.image.load("player/player_ship.png").convert_alpha()
player_ship_image = pygame.transform.scale(player_ship_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_rect = player_ship_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT))

# --- NEW: Create the separate hitbox rect ---
player_hitbox_rect = pygame.Rect(0, 0, PLAYER_HITBOX_WIDTH, PLAYER_HITBOX_HEIGHT)
player_hitbox_rect.center = player_rect.center # Center it initially

background = pygame.image.load("other_assets/background.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

player_bullet_image = pygame.image.load("player/bullet.png").convert_alpha()
player_bullet_image = pygame.transform.scale(player_bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))
player_bullets = []

enemy_bullet_image = pygame.image.load("enemies/enemy_bullet.png").convert_alpha()
enemy_bullet_image = pygame.transform.scale(enemy_bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))
enemy_bullets = [] # List will store dicts: {'rect': rect, 'vx': vx, 'vy': vy}

enemy_ship_image = pygame.image.load("enemies/enemy_ship.png").convert_alpha()
enemy_ship_image = pygame.transform.scale(enemy_ship_image, (ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT))
enemy_ship_rect = enemy_ship_image.get_rect(center=(SCREEN_WIDTH / 2, 100))
enemy_target_pos = None

# Load the sound effects
player_laser_sound_effect = pygame.mixer.Sound("player/player_laser.mp3")
player_laser_sound_effect.set_volume(0.1)
enemy_laser_sound_effect = pygame.mixer.Sound("enemies/enemy_laser.mp3")
enemy_laser_sound_effect.set_volume(0.1)
enemy_death_sound_effect = pygame.mixer.Sound("enemies/enemy_death.mp3")
enemy_death_sound_effect.set_volume(0.2)
player_death_sound_effect = pygame.mixer.Sound("player/player_death.mp3")

# Font for text
mono_font = pygame.font.SysFont("monospace", SCORE_FONT_SIZE)

# --- Initialize Timers ---
player_ship_fire_timer = 0
enemy_ship_fire_timer = 0
enemy_special_attack_timer = 0

def get_new_enemy_target():
    """Generates a new random target for the enemy in the top half of the screen."""
    x = random.randint(ENEMY_SHIP_WIDTH // 2, SCREEN_WIDTH - ENEMY_SHIP_WIDTH // 2)
    y = random.randint(ENEMY_SHIP_HEIGHT // 2, SCREEN_HEIGHT // 2)
    return [x, y]

def reset_game() -> None:
    """Resets the game to its initial state."""
    global player_bullets, enemy_bullets, player_health, enemy_health, game_over, victory, player_ship_fire_timer, enemy_ship_fire_timer, enemy_special_attack_timer, enemy_target_pos

    player_bullets = []
    enemy_bullets = []
    player_health = PLAYER_MAX_HEALTH
    enemy_health = ENEMY_MAX_HEALTH
    
    player_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT)
    enemy_ship_rect.center = (SCREEN_WIDTH / 2, 100)
    
    player_ship_fire_timer = 0
    enemy_ship_fire_timer = 0
    enemy_special_attack_timer = 0
    enemy_target_pos = get_new_enemy_target()
    
    game_over = False
    victory = False

# Set initial enemy target
enemy_target_pos = get_new_enemy_target()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and (game_over or victory):
             reset_game()

    if not game_over and not victory:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_rect.y -= PLAYER_SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_rect.y += PLAYER_SPEED
            
        if keys[pygame.K_SPACE] and player_ship_fire_timer >= PLAYER_FIRE_PAUSE:
            player_ship_fire_timer = 0
            bullet_rect = player_bullet_image.get_rect(midbottom=player_rect.midtop)
            player_bullets.append(bullet_rect)
            player_laser_sound_effect.play()

        player_ship_fire_timer += 1
        enemy_ship_fire_timer += 1
        enemy_special_attack_timer += 1
        
        player_rect.clamp_ip(screen.get_rect())

        # --- NEW: Update the hitbox position to follow the player sprite ---
        player_hitbox_rect.center = player_rect.center

        # --- Enemy AI Movement ---
        dx = enemy_target_pos[0] - enemy_ship_rect.centerx
        dy = enemy_target_pos[1] - enemy_ship_rect.centery
        dist = math.hypot(dx, dy)

        if dist < ENEMY_SPEED * 2: 
            enemy_target_pos = get_new_enemy_target()
        else:
            enemy_ship_rect.x += (dx / dist) * ENEMY_SPEED
            enemy_ship_rect.y += (dy / dist) * ENEMY_SPEED
            
        for b_rect in player_bullets[:]:
            b_rect.y -= PLAYER_BULLET_SPEED
            if b_rect.bottom < 0:
                player_bullets.remove(b_rect)

        for b in enemy_bullets[:]:
            b['rect'].x += b['vx']
            b['rect'].y += b['vy']
            if not screen.get_rect().colliderect(b['rect']):
                enemy_bullets.remove(b)

        if enemy_ship_fire_timer >= ENEMY_FIRE_PAUSE:
            enemy_ship_fire_timer = 0
            bullet_rect = enemy_bullet_image.get_rect(midtop=enemy_ship_rect.midbottom)
            enemy_bullets.append({'rect': bullet_rect, 'vx': 0, 'vy': ENEMY_BULLET_SPEED})
            enemy_laser_sound_effect.play()
            
        if enemy_special_attack_timer >= ENEMY_SPECIAL_ATTACK_COOLDOWN:
            enemy_special_attack_timer = 0
            enemy_laser_sound_effect.play()
            for i in range(8):
                angle = i * (math.pi / 4)
                vx = math.cos(angle) * ENEMY_BULLET_SPEED
                vy = math.sin(angle) * ENEMY_BULLET_SPEED
                bullet_rect = enemy_bullet_image.get_rect(center=enemy_ship_rect.center)
                enemy_bullets.append({'rect': bullet_rect, 'vx': vx, 'vy': vy})

        # --- Collision Detection ---
        for b_rect in player_bullets[:]:
            if enemy_ship_rect.colliderect(b_rect):
                player_bullets.remove(b_rect)
                enemy_health -= BULLET_DAMAGE
                enemy_death_sound_effect.play()
                if enemy_health <= 0:
                    victory = True
                break
        
        # --- CHANGED: Use the smaller hitbox for collision ---
        for b in enemy_bullets[:]:
            if player_hitbox_rect.colliderect(b['rect']):
                enemy_bullets.remove(b)
                player_health -= BULLET_DAMAGE
                if player_health <= 0:
                    game_over = True
                    player_death_sound_effect.play()
                break

        # --- Drawing ---
        screen.blit(background, (0, 0))
        screen.blit(player_ship_image, player_rect)
        screen.blit(enemy_ship_image, enemy_ship_rect)

        for b_rect in player_bullets:
            screen.blit(player_bullet_image, b_rect)
        for b in enemy_bullets:
            screen.blit(enemy_bullet_image, b['rect'])

        # --- OPTIONAL: Draw the hitbox for debugging. Comment this out for the final game. ---
        pygame.draw.rect(screen, (255, 0, 0), player_hitbox_rect, 2)


        player_health_bar = pygame.Rect(10, SCREEN_HEIGHT - 30, (player_health / PLAYER_MAX_HEALTH) * (SCREEN_WIDTH - 20), 20)
        pygame.draw.rect(screen, (0, 255, 0), player_health_bar)
        
        enemy_health_bar = pygame.Rect(10, 10, (enemy_health / ENEMY_MAX_HEALTH) * (SCREEN_WIDTH - 20), 20)
        pygame.draw.rect(screen, (255, 0, 0), enemy_health_bar)

    elif game_over:
        dead_label = mono_font.render("YOU HAVE DIED", 1, (255, 255, 255))
        play_again_label = mono_font.render("CLICK ANYWHERE TO PLAY AGAIN", 1, (255, 255, 255))
        screen.blit(dead_label, dead_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30)))
        screen.blit(play_again_label, play_again_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30)))
    
    elif victory:
        victory_label = mono_font.render("YOU ARE VICTORIOUS!", 1, (255, 255, 255))
        play_again_label = mono_font.render("CLICK ANYWHERE TO PLAY AGAIN", 1, (255, 255, 255))
        screen.blit(victory_label, victory_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30)))
        screen.blit(play_again_label, play_again_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()