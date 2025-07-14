"""
Following the trend, this will be a minigame, will have to make a victory/defeat 
"""
"""this one will be space invaders of a sort"""
import pygame
import random

# pygame setup
pygame.init()
pygame.mixer.init()

# Game attributes
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 1280
PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150

BULLET_WIDTH, BULLET_HEIGHT = 50, 100
BULLET_SPEED = 3

ENEMY_SHIP_WIDTH, ENEMY_SHIP_HEIGHT = 110, 110
ENEMY_SHIP_CENTER_LEFT_BOUND = 0
ENEMY_SHIP_CENTER_RIGHT_BOUND = SCREEN_WIDTH - (ENEMY_SHIP_WIDTH)
ENEMY_SHIP_SPEED = 0.5
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

'''for loop this'''
choice = random. randint(1, 100)
choice = random. choice(1, 100)

