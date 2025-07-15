import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.SysFont("Helvetica", 20)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

run = True
while run:

  screen.fill((255, 255, 255))
#__________
class Fernando:
    condition = False
    #Collection of Dialogue Bools
    #Tree1
    case1 = True #Things like this keep the dialogue from repeating
    case4 = True
     
    tree1 = False #Keeps player in the dialogue tree
    tree11 = False
    tree1Sec1 = False #Secret toggles

    portNo = True #Portrait toggle

    while not condition:
        tree1 = False
        if portNo == True:
            draw_text("welcome to Dandelion stranger! My name's Fernando! From the looks of it, you must be another one of those warriors.", text_font, (0, 0, 0), 20, 20)
            draw_text("Lots of your type around here. Some knights came by earlier, looking for the same things as you I bet.", text_font, (0, 0, 0), 20, 40)
            draw_text("*He gives a warm smile.", text_font, (0, 0, 0), 20, 20)
        portNo = True
        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 60)
        draw_text('(1) "What do you do?"', text_font, (0, 0, 0), 20, 80)
        draw_text('(2) "Where can I rest?"', text_font, (0, 0, 0), 20, 100)
        draw_text('(3) "Knights?"', text_font, (0, 0, 0), 20, 120)
        draw_text('(4) "What can you tell me about this place?"', text_font, (0, 0, 0), 20, 140)
        draw_text('(5) Fight Fernando', text_font, (0, 0, 0), 20, 160)
        draw_text('(6) Leave', text_font, (0, 0, 0), 20, 180)
        Uinput = float(input())
        while not tree1:
            match Uinput: #Dialogue tree
                case 1:
                    tree1 = False
                    tree11 = False
                    if case1 == True:
                        draw_text("As you can see, I'm a farmhand. The farm's about a few fields down, where I help with the grain and cattle.", text_font, (0, 0, 0), 20, 20)
                        draw_text("It's fine work I tell you. You'd feel sore by the end of the day, but I'd say it's worth breaking", text_font, (0, 0, 0), 20, 40)
                        draw_text("your back in order to feed the entire town.", text_font, (0, 0, 0), 20, 20)
                        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 60)
                    elif case1 == False:
                        draw_text("*Fernando leans on his pitchfork", text_font, (0, 0, 0), 20, 20)
                        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)
                    else:
                        tree1 = True
                    #Responses
                    while not tree11:
                        draw_text('(1) "Have you had any trouble farming lately?"', text_font, (0, 0, 0), 20, 20)
                        draw_text('(2) "Any other farmers around here?"', text_font, (0, 0, 0), 20, 20)
                        draw_text("(3) Back", text_font, (0, 0, 0), 20, 20)
                        if tree1Sec1 == True:
                            draw_text('(4) How bad was the attack?', text_font, (0, 0, 0), 20, 20)

                        Uinput = float(input())
                        match Uinput:
                            case 1:
                                draw_text("Oh yes! It's been hell on Earth for us ever since these monsters showed on up.", text_font, (0, 0, 0), 20, 20)
                                draw_text("We try to run them off, but they come in great numebers. It doesn't help that they come after dusk too.", text_font, (0, 0, 0), 20, 20)
                                draw_text("We're scared for our lives. They know our food's a target, and they're a very relentless mob indeed.", text_font, (0, 0, 0), 20, 20)
                                draw_text("*He leans on his pitchfork heavily", text_font, (0, 0, 0), 20, 20)
                                draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)
                                case1 = False
                                tree1Sec1 = True
                            case 2:
                                draw_text("Most of them are still at the farm working. I'm here because I was set on the lookout.", text_font, (0, 0, 0), 20, 20)
                                draw_text("The last attack was the worst we ever got it. We have to spread ourselves thin to", text_font, (0, 0, 0), 20, 20)
                                draw_text("make up for the lost men.", text_font, (0, 0, 0), 20, 20)
                                draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)

                            case 3:
                                tree1 = True
                                tree11 = True
                            case 4:
                                if tree1Sec1 == True:
                                    draw_text("It was terrible. About 13 were lost during the attack, including a mother and father.", text_font, (0, 0, 0), 20, 20)
                                    draw_text("People are sick with grief. I wish I could do more to help them. I really do.", text_font, (0, 0, 0), 20, 20)
                                    
                case 2:
                    draw_text("You can rest at the inn just a little further in. It says Catcher Sam's at the top. Couldn't miss it.", text_font, (0, 0, 0), 20, 20)
                    portNo = False
                    tree1 = True  
                case 3:
                    draw_text("That's right. They're knights sent straight from the baron, so they're the best we're going to have it.", text_font, (0, 0, 0), 20, 20)
                    draw_text("Their captain was named Hannibal. I think he's somewhere in the town.", text_font, (0, 0, 0), 20, 20)
                    draw_text("You won't find many though. I heared they were hurt really bad since their last adventure in that cave.", text_font, (0, 0, 0), 20, 20)
                    draw_text("May God rest their souls.", text_font, (0, 0, 0), 20, 20)
                    portNo = False
                    tree1 = True            
                case 4: #case4
                    tree1 = False
                    tree11 = False
                    if case4 == True:
                        draw_text("Well, there's a lot I could say. Depends on what you want to know!", text_font, (0, 0, 0), 20, 20)
                        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)
                    elif case4 == False:
                        draw_text("*Fernando leans on his pitchfork", text_font, (0, 0, 0), 20, 20)
                        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)
                    else:
                        tree1 = True
                    #Responses
                    while not tree11:
                        draw_text("---------------------------------------------------------------------------------------------", text_font, (0, 0, 0), 20, 20)
                        draw_text('(1) "Where can I buy armor and weapons?"', text_font, (0, 0, 0), 20, 20)
                        draw_text('(2) "Where can I buy healing items?"', text_font, (0, 0, 0), 20, 20)
                        draw_text('(3) "why is this place named Dandelion?"', text_font, (0, 0, 0), 20, 20)
                        draw_text("(4) Back", text_font, (0, 0, 0), 20, 20)
                        Uinput = float(input())
                        match Uinput:
                            case 1:
                                draw_text("From the square there should be a large grey buidling with shingles on the side.", text_font, (0, 0, 0), 20, 20)
                                draw_text("Just walk into the dullest building you see and you'll probably find it.", text_font, (0, 0, 0), 20, 20)
                                draw_text("It's ran by Andre. Great guy. He sells most of the wares we have available.", text_font, (0, 0, 0), 20, 20)
                            case 2:
                                draw_text("Oh yeah... I haven't been there in ages. I can't exactly remember.", text_font, (0, 0, 0), 20, 20)
                                draw_text("Try asking Andre, he's the main shopkeeper around here.", text_font, (0, 0, 0), 20, 20)
                            case 3:
                                draw_text("It means 'lion's tooth.' Natives of this land used to trade accessories made", text_font, (0, 0, 0), 20, 20)
                                draw_text("out of teeth of mighty cats, many of which were lions.", text_font, (0, 0, 0), 20, 20)
                                draw_text("Our village used to be a trading post for such items. Eventually, we became a town.", text_font, (0, 0, 0), 20, 20)
                            case 4:
                                tree1 = True
                                tree11 = True
                case 5:
                    draw_text('"AAAAAAAH"', text_font, (0, 0, 0), 20, 20)
                    condition = True
                    #Adding combat code later. Hoping Pablo cooks fr.
                case 6:
                    condition = True
#__________
draw_text("Hello World", text_font, (0, 0, 0), 20, 20)
draw_text("Hello World", text_font, (0, 0, 0), 20, 40)

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False

  pygame.display.flip()

pygame.quit()