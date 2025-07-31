import pygame
import time
import subprocess
import FernandoDialogue

def game():
  pygame.init()
  
  SCREEN_WIDTH = 600
  SCREEN_HEIGHT = 400
  
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
      Dand = pygame.image.load("Dandelion.jpg")
      startButton = pygame.image.load("startButton.jpg")
      Dand2 = pygame.transform.scale(Dand, (50, 50))
      startButton2 = pygame.transform.scale(startButton, (100, 100))
  
      screen.blit(Dand, (100, 50))
      screen.blit(startButton2, (250, 280))
  
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
  
  #Start GAME
  pygame.init()
  
  SCREEN_WIDTH = 600
  SCREEN_HEIGHT = 400
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  text_font = pygame.font.SysFont("Helvetica", 20)
  
  #function for outputting text onto the screen
  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
  
  screen.fill((0, 0, 0))
  startGame2 = True
  while startGame2:
      draw_text("Welcome Traveler!", text_font, (255, 255, 255), 20, 20)
      lightPause = pygame.time.get_ticks() #Pause in between dialogue
      mathPause = (lightPause % 1000)
      if lightPause >= 2000:
          draw_text("You're arriving back from your most recent campaign...", text_font, (255, 255, 255), 20, 40)
      if lightPause >= 4000:
          draw_text("There's a town over in the horizon!", text_font, (255, 255, 255), 20, 60)
      if lightPause >= 8000:
          draw_text("Press E to continue!", text_font, (255, 255, 255), 20, 80)
  
      Villa = pygame.image.load("villa.jpg")
      Villa2 = pygame.transform.scale(Villa, (50, 50))
      opaLoop = 3
      opa = 5
      for i in range(8):
              opa ** i
              pygame.Surface.set_alpha(Villa, opa)
              if mathPause == 0:
                  screen.blit(Villa, (200, 150))
  
      
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_e:
                  startGame2 = False
    #draw_text("Hello World", text_font, (0, 0, 0), 20, 20)
    #draw_text("Hello World", text_font, (0, 0, 0), 20, 40)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              startGame2 = False
  
      pygame.display.flip()
  pygame.quit()
  
  print("Running FernandoDialogue")
  input("Press Enter twice in terminal to open...")
  FernandoDialogue.fernando()
  #if input() == "e": 
  