"""
Following the trend, this will be a minigame, will have to make a victory/defeat 
"""
"""this one will be space invaders of a sort"""
import pygame
import random
from time import *

# pygame setup
pygame.init()
pygame.mixer.init()

choice = random.randint(1, 100)
# choice = random.choice(1, 100)

# Game attributes
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 1000
PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150

BULLET_WIDTH, BULLET_HEIGHT = 50, 100
BULLET_SPEED = 3

ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT = 110, 110
ENEMY_SHIP_CENTER_LEFT_BOUND = 0
ENEMY_SHIP_CENTER_RIGHT_BOUND = SCREEN_WIDTH - (ENEMY_SHIP_WIDTH)
ENEMY_SHIP_SPEED = 0.3
ENEMY_SHIP_MAX_LEFT_SHIFT = -(3 * BULLET_WIDTH)
ENEMY_SHIP_MAX_RIGHT_SHIFT = (3 * BULLET_WIDTH)
ENEMY_FIRE_PAUSE = 200

SCORE_FONT_SIZE = 30

# use to track hits without a health system for the enemies??
SCORE_TO_SHIP_RATIO = 10

HITBOX_BUFFER = 65
X_BUFFER = 30
LOOPS_UNTIL_ENEMY_SHIP_MOVES_HORIZONTALLY = choice
SATISFACTION = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score = 0
dead = False
clock = pygame.time.Clock()
running = True

# Load images
player_ship = pygame.image.load("player/player_ship.png").convert_alpha()
player_ship = pygame.transform.scale(player_ship, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_rect = player_ship.get_rect()

background = pygame.image.load("other_assets/background.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

bullet = pygame.image.load("player/bullet.png").convert_alpha()
bullet = pygame.transform.scale(bullet, (BULLET_WIDTH, BULLET_HEIGHT))
bullet_locations = []

enemy_bullet = pygame.image.load("enemies/enemy_bullet.png").convert_alpha()
enemy_bullet = pygame.transform.scale(enemy_bullet, (BULLET_WIDTH, BULLET_HEIGHT))
enemy_bullet_locations = []

enemy_ship = pygame.image.load("enemies/enemy_ship.png").convert_alpha()
enemy_ship = pygame.transform.scale(enemy_ship, (ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT))
enemy_ship_locations = []
enemy_ship_fire_timers = []

# Load the sound effects
"""
Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=14562">freesound_community</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=14562">Pixabay</a>
"""
player_laser_sound_effect = pygame.mixer.Sound("player/player_laser.mp3")
player_laser_sound_effect.set_volume(0.1)
"""
Sound Effect by <a href="https://pixabay.com/users/driken5482-45721595/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=236669">Driken Stan</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=236669">Pixabay</a>
"""
enemy_laser_sound_effect = pygame.mixer.Sound("enemies/enemy_laser.mp3")
enemy_laser_sound_effect.set_volume(0.1)
"""
Sound Effect by <a href="https://pixabay.com/users/u_b32baquv5u-50250111/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=340460">u_b32baquv5u</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=340460">Pixabay</a>
"""
enemy_death_sound_effect = pygame.mixer.Sound("enemies/enemy_death.mp3")
enemy_death_sound_effect.set_volume(0.2)
"""
Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=66829">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=66829">Pixabay</a>
"""
player_death_sound_effect = pygame.mixer.Sound("player/player_death.mp3")

# Font for text
mono_font = pygame.font.SysFont("monospace", SCORE_FONT_SIZE)
score_label = mono_font.render("Score: 0", 1, (255, 255, 255))

def entity_hit(entity_x: float, entity_width: float,
              entity_y: float, entity_height: float, 
              bullet_x: float, bullet_width: float,
              bullet_y: float, bullet_height: float, hitbox_buffer: float) -> bool:
    """
    Checks if the bullet has hit the entity

    Args:
    - entity_x (float): x position of the entity rect
    - entity_wdith (float): width of the entity
    - entity_y (float): y position of the entity rect
    - entity_height (float): height of the entity
    - bullet_x (float): x position of the bullet rect
    - bullet_width (float): width of the bullet
    - bullet_y (float): y position of the bullet rect
    - bullet_height (float): height of the bullet
    - hitbox_buffer (float): vertical hitbox buffer to account for empty space in sprites

    Returns:
    - a boolean (if hit -> True, if no hit -> False)
    """

    horizontal_condition_one = (entity_x + X_BUFFER < bullet_x < entity_x + entity_width - X_BUFFER)
    horizontal_condition_two = (entity_x + X_BUFFER < bullet_x + bullet_width < entity_x + entity_width - X_BUFFER)
    horizontal_met = horizontal_condition_one or horizontal_condition_two

    vertical_condition_one = (entity_y - hitbox_buffer < bullet_y < entity_y + entity_height - hitbox_buffer)
    vertical_condition_two = (entity_y - hitbox_buffer < bullet_y + bullet_height < entity_y + entity_height - hitbox_buffer)
    vertical_met = vertical_condition_one or vertical_condition_two


    return horizontal_met and vertical_met

def reset_game() -> None:
    """
    Resets everything

    Args:
    - None

    Returns:
    - None
    """

    global bullet_locations, enemy_bullet_locations, enemy_ship_locations, \
    enemy_ship_fire_timers, score, dead

    bullet_locations = []
    enemy_bullet_locations = []
    enemy_ship_locations = []
    enemy_ship_fire_timers = []
    score = 0
    dead = False


# Ship data
player_x_center = SCREEN_WIDTH / 2
player_y_center = SCREEN_HEIGHT - (player_ship.get_height() / 2)

loop_counter = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not dead:
                # If the mouse is clicked (down stroke), make a bullet
                bullet_location_x = player_x_center - (BULLET_WIDTH / 2)
                bullet_location_y = player_y_center - (PLAYER_HEIGHT / 2)

                bullet_locations.append([bullet_location_x, bullet_location_y])
                player_laser_sound_effect.play()
            else:
                reset_game()

    if not dead:
        # Adjust bullet locations
        for index in range(len(bullet_locations)-1, -1, -1):
            bullet_locations[index][1] -= BULLET_SPEED

            # Check for out of bounds
            if bullet_locations[index][1] < 0:
                del bullet_locations[index]

        # Adjust enemy bullet locations
        for index in range(len(enemy_bullet_locations)-1, -1, -1):
            enemy_bullet_locations[index][1] += BULLET_SPEED

            # Check for out of bounds
            if enemy_bullet_locations[index][1] + BULLET_HEIGHT >= SCREEN_HEIGHT:
                del enemy_bullet_locations[index]

        # Adjust enemy ship locations
        for index in range(len(enemy_ship_locations)-1, -1, -1):
            enemy_ship_locations[index][1] += ENEMY_SHIP_SPEED

            # Randomly shift to the side
            left_x_available_space = enemy_ship_locations[index][0]
            right_x_available_space = SCREEN_WIDTH - (enemy_ship_locations[index][0] + ENEMY_SHIP_WIDTH)

            left_shift_bound = max(-left_x_available_space, ENEMY_SHIP_MAX_LEFT_SHIFT)
            right_shift_bound = min(right_x_available_space, ENEMY_SHIP_MAX_RIGHT_SHIFT)

            distance_moved = left_shift_bound + (random.random() * (right_shift_bound - left_shift_bound))

            # Buffer side to side movement to avoid laggy look
            if loop_counter == 0:
                enemy_ship_locations[index][0] += distance_moved

            # Update fire timer
            if enemy_ship_fire_timers[index] == ENEMY_FIRE_PAUSE:
                # Make the bullet
                enemy_bullet_x = enemy_ship_locations[index][0] + (ENEMY_SHIP_WIDTH / 2)
                enemy_bullet_y = enemy_ship_locations[index][1] + (ENEMY_SHIP_HEIGHT)

                enemy_bullet_locations.append([enemy_bullet_x, enemy_bullet_y])
                enemy_laser_sound_effect.play()

                # Reset the pause timer
                enemy_ship_fire_timers[index] = 0
            else:
                enemy_ship_fire_timers[index] += 1

            # Check for out of bounds
            if enemy_ship_locations[index][1] + ENEMY_SHIP_HEIGHT >= SCREEN_HEIGHT - PLAYER_HEIGHT:
                del enemy_ship_locations[index]
                del enemy_ship_fire_timers[index]

        # Determine enemy location spawn points
        if len(enemy_ship_locations) < ((score // SCORE_TO_SHIP_RATIO) + 1):
            enemy_possible_x_span = ENEMY_SHIP_CENTER_RIGHT_BOUND - ENEMY_SHIP_CENTER_LEFT_BOUND
            enemy_ship_x = ENEMY_SHIP_CENTER_LEFT_BOUND + (random.random() * enemy_possible_x_span)

            enemy_ship_y = 0

            # Add ship and fire timer
            enemy_ship_locations.append([enemy_ship_x, enemy_ship_y])
            enemy_ship_fire_timers.append(0)

        # Check for bullet collision
        for bullet_index in range(len(bullet_locations)-1, -1, -1):
            for enemy_index in range(len(enemy_ship_locations)-1, -1, -1):
                # Extract the info
                bullet_x, bullet_y = bullet_locations[bullet_index]
                enemy_x, enemy_y = enemy_ship_locations[enemy_index]

                # If hit, remove the enemy and the ship
                if entity_hit(enemy_x, ENEMY_SHIP_WIDTH, enemy_y, ENEMY_SHIP_HEIGHT,
                            bullet_x, BULLET_WIDTH, bullet_y, BULLET_HEIGHT, HITBOX_BUFFER):
                    del bullet_locations[bullet_index]
                    del enemy_ship_locations[enemy_index]
                    score += 1
                    enemy_death_sound_effect.play()

                    break

        for enemy_bullet_index in range(len(enemy_bullet_locations)-1, -1, -1):
            # Extract the info
            bullet_x, bullet_y = enemy_bullet_locations[enemy_bullet_index]

            # If an enemy bullet hits a player
            if entity_hit(player_x_center - (PLAYER_WIDTH/2), PLAYER_WIDTH, player_y_center-(PLAYER_HEIGHT/2), PLAYER_HEIGHT,
                        bullet_x, BULLET_WIDTH, bullet_y, BULLET_HEIGHT, -HITBOX_BUFFER):
                dead = True
                player_death_sound_effect.play()
        
        # Have the ship's x be aligned with the mouse position
        player_x_center = pygame.mouse.get_pos()[0]

        # Adjust and draw the ship
        player_rect.center = [player_x_center, player_y_center]
        screen.blit(background, (0, 0))
        screen.blit(player_ship, player_rect)

        # Draw the enemies
        for enemy_ship_location in enemy_ship_locations:
            screen.blit(enemy_ship, enemy_ship_location)

        # Draw the bullets, if any
        for bullet_location in bullet_locations:
            screen.blit(bullet, bullet_location)
        for enemy_bullet_location in enemy_bullet_locations:
            screen.blit(enemy_bullet, enemy_bullet_location)

        # Update and draw the score
        score_label = mono_font.render(f"Score: {score * SATISFACTION}", 1, (255, 255, 255))
        screen.blit(score_label, (0, 0))

    else:
        dead_label = mono_font.render("YOU HAVE DIED", 1, (255, 255, 255))
        dead_label_x = (SCREEN_WIDTH / 2) - (dead_label.get_width() / 2)
        dead_label_y = (SCREEN_HEIGHT / 2) - (dead_label.get_height())
        screen.blit(dead_label, (dead_label_x, dead_label_y))

        play_again_label = mono_font.render("CLICK ANYWHERE TO PLAY AGAIN", 1, (255, 255, 255))
        play_again_label_x = (SCREEN_WIDTH / 2) - (play_again_label.get_width() / 2)
        play_again_label_y = (SCREEN_HEIGHT / 2) + (play_again_label.get_height())
        screen.blit(play_again_label, (play_again_label_x, play_again_label_y))
    
    pygame.display.flip()
    loop_counter = (loop_counter + 1) % LOOPS_UNTIL_ENEMY_SHIP_MOVES_HORIZONTALLY


pygame.quit()