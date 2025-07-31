import pygame
import random
import math
from time import *
import os # <-- PLEASE WORK

# --- Get the directory of the script to build reliable paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))

def game():
    # pygame setup
    pygame.init()
    pygame.mixer.init()

    # special attack booleans
    firebomb_special = False
    heal_flask = False

    # --- Use os.path.join to create reliable file paths ---
    inv = os.path.join(script_dir, "text", "inv.txt")
    death = os.path.join(script_dir, "text", "death.txt")
    try:
        with open(inv, 'r') as file:
            # Initialize default stats
            atk, spd, spdP, spd_player, hp_player = 10, 10, 30, 5, 100
            for line in file:
                match line.strip():
                    case "longsword":
                        atk, spd, spdP, spd_player, hp_player = 10, 10, 30, 5, 100
                    case "dagger":
                        atk, spd, spdP, spd_player, hp_player = 5, 15, 20, 5, 100
                    case "staff":
                        atk, spd, spdP, spd_player, hp_player = 20, 5, 60, 5, 100
                    case "firebomb":
                        firebomb_special = True
                    case "flask":
                        heal_flask = True
                    case "crowbar":
                        atk += 2
                        spd += 2
                        spd_player += 5
                    case "greatcoat":
                        hp_player += 25
                        spd_player -= 1
                    case "leathergloves":
                        atk += 2
                        spd += 2
                        spdP -= 4
                    case "bowgun":
                        atk += 10
                        spd += 3
                        spdP += 15
                    case "jackknife":
                        atk += 4
                        spd += 5
                    case "greathelm":
                        hp_player += 15
                    case "leatherboots":
                        hp_player += 10
                        spd_player += 1
    except FileNotFoundError:
        print(f"Error: The inventory file was not found at {inv}")
        print("Using default stats.")
        atk, spd, spdP, spd_player, hp_player = 10, 10, 30, 5, 100


    # Game attributes
    SCREEN_WIDTH, SCREEN_HEIGHT = 720, 900
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_HITBOX_WIDTH = PLAYER_WIDTH // 3
    PLAYER_HITBOX_HEIGHT = PLAYER_HEIGHT // 3
    PLAYER_MAX_HEALTH = hp_player
    PLAYER_SPEED = spd_player
    player_health = PLAYER_MAX_HEALTH

    BULLET_WIDTH, BULLET_HEIGHT = 50, 100
    PLAYER_BULLET_SPEED = spd
    ENEMY_BULLET_SPEED = 9
    PLAYER_BULLET_DAMAGE = atk
    ENEMY_BULLET_DAMAGE = 10
    PLAYER_FIRE_PAUSE = spdP

    BEAM_DURATION = 30
    BEAM_WIDTH = 20
    BEAM_DAMAGE_PER_FRAME = 1.5
    BEAM_COLOR = (0, 255, 255)

    SPECIAL_ABILITY_COOLDOWN = 300

    player_ship_2_WIDTH, player_ship_2_HEIGHT = 110, 110
    ENEMY_SPEED = 5
    ENEMY_FIRE_PAUSE = 70
    ENEMY_SPECIAL_ATTACK_COOLDOWN = 180
    ENEMY_MAX_HEALTH = 200
    enemy_health = ENEMY_MAX_HEALTH

    SCORE_FONT_SIZE = 30

    COOLDOWN_BAR_WIDTH = 200
    COOLDOWN_BAR_HEIGHT = 25
    COOLDOWN_BAR_X = (SCREEN_WIDTH - COOLDOWN_BAR_WIDTH) / 2
    COOLDOWN_BAR_Y = SCREEN_HEIGHT - 50
    COOLDOWN_BAR_COLOR_BG = (50, 50, 50)
    COOLDOWN_BAR_COLOR_FG = (255, 215, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_over = False
    victory = False
    clock = pygame.time.Clock()
    running = True

    # --- Load assets using the os.path.join method ---
    try:
        player_ship_image = pygame.image.load(os.path.join(script_dir, "player", "player_ship.png")).convert_alpha()
        background = pygame.image.load(os.path.join(script_dir, "other_assets", "background.jpg")).convert()
        player_bullet_image = pygame.image.load(os.path.join(script_dir, "player", "bullet.png")).convert_alpha()
        enemy_bullet_image = pygame.image.load(os.path.join(script_dir, "enemies", "enemy_bullet.png")).convert_alpha()
        player_ship_2_image = pygame.image.load(os.path.join(script_dir, "enemies", "player_ship_2.png")).convert_alpha()
        
        player_laser_sound_effect = pygame.mixer.Sound(os.path.join(script_dir, "player", "player_laser.mp3"))
        player_beam_sound_effect = pygame.mixer.Sound(os.path.join(script_dir, "player", "beam.mp3"))
        enemy_laser_sound_effect = pygame.mixer.Sound(os.path.join(script_dir, "enemies", "enemy_laser.mp3"))
        enemy_death_sound_effect = pygame.mixer.Sound(os.path.join(script_dir, "enemies", "enemy_death.mp3"))
        player_death_sound_effect = pygame.mixer.Sound(os.path.join(script_dir, "player", "player_death.mp3"))
    except pygame.error as e:
        print(f"Fatal Error: Could not load one or more assets. {e}")
        print("Please ensure your asset folders (player, enemies, etc.) are in the same directory as the script.")
        return

    # Scale images
    player_ship_image = pygame.transform.scale(player_ship_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    player_bullet_image = pygame.transform.scale(player_bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))
    enemy_bullet_image = pygame.transform.scale(enemy_bullet_image, (BULLET_WIDTH, BULLET_HEIGHT))
    player_ship_2_image = pygame.transform.scale(player_ship_2_image, (player_ship_2_WIDTH, player_ship_2_HEIGHT))

    player_rect = player_ship_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT))
    player_hitbox_rect = pygame.Rect(0, 0, PLAYER_HITBOX_WIDTH, PLAYER_HITBOX_HEIGHT)
    player_hitbox_rect.center = player_rect.center
    
    player_bullets = []
    enemy_bullets = []
    player_ship_2_rect = player_ship_2_image.get_rect(center=(SCREEN_WIDTH / 2, 100))
    enemy_target_pos = None

    player_laser_sound_effect.set_volume(0.1)
    enemy_laser_sound_effect.set_volume(0.1)
    enemy_death_sound_effect.set_volume(0.2)

    mono_font = pygame.font.SysFont("monospace", SCORE_FONT_SIZE)
    small_font = pygame.font.SysFont("monospace", 18)

    player_ship_fire_timer = 0
    player_ship_2_fire_timer = 0
    enemy_special_attack_timer = 0
    special_ability_timer = SPECIAL_ABILITY_COOLDOWN
    beam_active = False
    beam_duration_timer = 0
    beam_rect = pygame.Rect(0, 0, BEAM_WIDTH, SCREEN_HEIGHT)

    def get_new_enemy_target():
        x = random.randint(player_ship_2_WIDTH // 2, SCREEN_WIDTH - player_ship_2_WIDTH // 2)
        y = random.randint(player_ship_2_HEIGHT // 2, SCREEN_HEIGHT // 2)
        return [x, y]

    enemy_target_pos = get_new_enemy_target()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN and (game_over or victory) and event.button == 1: running = False

        if not game_over and not victory:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_o] and special_ability_timer >= SPECIAL_ABILITY_COOLDOWN:
                if firebomb_special:
                    beam_active = True
                    special_ability_timer = 0
                    beam_duration_timer = 0
                    player_beam_sound_effect.play()
                elif heal_flask:
                    player_health = min(PLAYER_MAX_HEALTH, player_health + 50)
                    special_ability_timer = 0

            if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_rect.x -= PLAYER_SPEED
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_rect.x += PLAYER_SPEED
            if keys[pygame.K_w] or keys[pygame.K_UP]: player_rect.y -= PLAYER_SPEED
            if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_rect.y += PLAYER_SPEED

            if keys[pygame.K_SPACE] and player_ship_fire_timer >= PLAYER_FIRE_PAUSE:
                player_ship_fire_timer = 0
                bullet_rect = player_bullet_image.get_rect(midbottom=player_rect.midtop)
                player_bullets.append(bullet_rect)
                player_laser_sound_effect.play()

            player_ship_fire_timer += 1
            player_ship_2_fire_timer += 1
            enemy_special_attack_timer += 1
            if special_ability_timer < SPECIAL_ABILITY_COOLDOWN:
                special_ability_timer += 1

            player_rect.clamp_ip(screen.get_rect())
            player_hitbox_rect.center = player_rect.center

            dx, dy = enemy_target_pos[0] - player_ship_2_rect.centerx, enemy_target_pos[1] - player_ship_2_rect.centery
            dist = math.hypot(dx, dy)
            if dist < ENEMY_SPEED: enemy_target_pos = get_new_enemy_target()
            else:
                player_ship_2_rect.x += (dx / dist) * ENEMY_SPEED
                player_ship_2_rect.y += (dy / dist) * ENEMY_SPEED

            for b_rect in player_bullets[:]:
                b_rect.y -= PLAYER_BULLET_SPEED
                if b_rect.bottom < 0: player_bullets.remove(b_rect)

            for b in enemy_bullets[:]:
                b['rect'].move_ip(b['vx'], b['vy'])
                if not screen.get_rect().colliderect(b['rect']): enemy_bullets.remove(b)

            if beam_active:
                beam_duration_timer += 1
                beam_rect.midbottom = player_rect.midtop
                if beam_rect.colliderect(player_ship_2_rect):
                    enemy_health -= BEAM_DAMAGE_PER_FRAME
                if beam_duration_timer >= BEAM_DURATION:
                    beam_active = False

            if player_ship_2_fire_timer >= ENEMY_FIRE_PAUSE:
                player_ship_2_fire_timer = 0
                bullet_rect = enemy_bullet_image.get_rect(midtop=player_ship_2_rect.midbottom)
                enemy_bullets.append({'rect': bullet_rect, 'vx': 0, 'vy': ENEMY_BULLET_SPEED})
                enemy_laser_sound_effect.play()

            if enemy_special_attack_timer >= ENEMY_SPECIAL_ATTACK_COOLDOWN:
                enemy_special_attack_timer = 0
                for i in range(8):
                    angle = i * (math.pi / 4)
                    vx = math.cos(angle) * ENEMY_BULLET_SPEED
                    vy = math.sin(angle) * ENEMY_BULLET_SPEED
                    bullet_rect = enemy_bullet_image.get_rect(center=player_ship_2_rect.center)
                    enemy_bullets.append({'rect': bullet_rect, 'vx': vx, 'vy': vy})

            if enemy_health <= 0: victory = True

            for b_rect in player_bullets[:]:
                if player_ship_2_rect.colliderect(b_rect):
                    player_bullets.remove(b_rect)
                    enemy_health -= PLAYER_BULLET_DAMAGE
                    enemy_death_sound_effect.play()
                    if enemy_health <= 0: victory = True; break

            for b in enemy_bullets[:]:
                if player_hitbox_rect.colliderect(b['rect']):
                    enemy_bullets.remove(b)
                    player_health -= ENEMY_BULLET_DAMAGE
                    if player_health <= 0: game_over = True; break

            screen.blit(background, (0, 0))
            screen.blit(player_ship_image, player_rect)
            screen.blit(player_ship_2_image, player_ship_2_rect)

            for b_rect in player_bullets: screen.blit(player_bullet_image, b_rect)
            for b in enemy_bullets: screen.blit(enemy_bullet_image, b['rect'])

            if beam_active: pygame.draw.rect(screen, BEAM_COLOR, beam_rect)

            player_health_bar = pygame.Rect(10, SCREEN_HEIGHT - 100, (player_health / PLAYER_MAX_HEALTH) * (SCREEN_WIDTH - 20), 20)
            pygame.draw.rect(screen, (0, 255, 0), player_health_bar)
            enemy_health_bar = pygame.Rect(10, 10, (enemy_health / ENEMY_MAX_HEALTH) * (SCREEN_WIDTH - 20), 20)
            pygame.draw.rect(screen, (255, 0, 0), enemy_health_bar)
            
            if firebomb_special or heal_flask:
                special_label = small_font.render("Special", 1, (255, 255, 255))
                screen.blit(special_label, (COOLDOWN_BAR_X - special_label.get_width() - 10, COOLDOWN_BAR_Y + 2))
                pygame.draw.rect(screen, COOLDOWN_BAR_COLOR_BG, (COOLDOWN_BAR_X, COOLDOWN_BAR_Y, COOLDOWN_BAR_WIDTH, COOLDOWN_BAR_HEIGHT))
                fill_width = (special_ability_timer / SPECIAL_ABILITY_COOLDOWN) * COOLDOWN_BAR_WIDTH
                pygame.draw.rect(screen, COOLDOWN_BAR_COLOR_FG, (COOLDOWN_BAR_X, COOLDOWN_BAR_Y, fill_width, COOLDOWN_BAR_HEIGHT))

        elif game_over:
            dead_label = mono_font.render("YOU HAVE DIED", 1, (255, 255, 255))
            screen.blit(dead_label, dead_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30)))
            try:
                with open(death, "w") as file: file.writelines("yes")
            except IOError: pass

        elif victory:
            victory_label = mono_font.render("YOU ARE VICTORIOUS!", 1, (255, 255, 255))
            play_again_label = mono_font.render("FERNANDO DIES", 1, (255, 255, 255))
            continue_play = mono_font.render("CLICK TO CONTINUE", 1, (255, 255, 255))
            screen.blit(victory_label, victory_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30)))
            screen.blit(play_again_label, play_again_label.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30)))
            screen.blit(continue_play, continue_play.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 60)))
            try:
                with open(death, "w") as file: file.writelines("no")
            except IOError: pass

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    game()