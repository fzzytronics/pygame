import pygame
import time

def game():
    pygame.init()

    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    text_font = pygame.font.SysFont("Helvetica", 20)

    #function for outputting text onto the screen
    def draw_text(text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      screen.blit(img, (x, y))

    screen.fill((0, 0, 0))
    startGame = True
    while startGame:
      for event in pygame.event.get():
        p1 = pygame.image.load(r"C:\Users\jaedyn mcneil\OneDrive\Desktop\pygame-main\GameTestFolder\images\villa.jpg")
        p2 = pygame.transform.scale(p1, (50, 50))

        screen.blit(p1, (0, 0))

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            startGame = False
      #draw_text("Hello World", text_font, (0, 0, 0), 20, 20)
      #draw_text("Hello World", text_font, (0, 0, 0), 20, 40)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          startGame = False

      pygame.display.flip()

    pygame.quit()