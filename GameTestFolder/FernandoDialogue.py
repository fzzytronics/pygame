import time


def fernando():
    Uinput = input()
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
            print("---------------------------------------------------------------------------------------------")
            print('               █████████████████████████')
            print('███████                            █████')
            print('███                                  ███')
            print('                                       █')
            print('                                        ')
            print('            █████████████████           ')
            print('       █████        █████  █ ███████    ')
            print('   ███████                   ██  ███  ')
            print('███████    ███   █████      ██         ')
            print('     ██  ██████     █████████            ')
            print('      █  █████       ██████              ')
            print('      ██████          ███               ')
            print('      ██                                ')
            print('      ██     ████                    █  ')
            print('      ██       ██                  ███  ')
            print('█ ██████                           █████')
            print('  ███████                          ████  ')
            print('       ███   ████████████████    ████   ')
            print('                               ████     ')
            print('         ████                ████       ')
            print('           █████         █████          ')
            print('                ██████                  ') 
            print("welcome to Dandelion stranger! My name's Fernando! From the looks of it, you must be another one of those warriors.")
            print("Lots of your type around here. Some knights came by earlier, looking for the same things as you I bet.")
            print("*He gives a warm smile.")
        portNo = True
        print("---------------------------------------------------------------------------------------------")
        print('(1) "What do you do?"')
        print('(2) "Where can I rest?"')
        print('(3) "Knights?"')
        print('(4) "What can you tell me about this place?"')
        print('(5) Fight Fernando')
        print('(6) Leave')
        Uinput = float(input())
        while not tree1:
            match Uinput: #Dialogue tree
                case 1:
                    tree1 = False
                    tree11 = False
                    if case1 == True:
                        print("As you can see, I'm a farmhand. The farm's about a few fields down, where I help with the grain and cattle.")
                        print("It's fine work I tell you. You'd feel sore by the end of the day, but I'd say it's worth breaking")
                        print("your back in order to feed the entire town.")
                        print("---------------------------------------------------------------------------------------------")
                    elif case1 == False:
                        print("*Fernando leans on his pitchfork")
                        print("---------------------------------------------------------------------------------------------")
                    else:
                        tree1 = True
                    #Responses
                    while not tree11:
                        print('(1) "Have you had any trouble farming lately?"')
                        print('(2) "Any other farmers around here?"')
                        print("(3) Back")
                        if tree1Sec1 == True:
                            print('(4) How bad was the attack?')

                        Uinput = float(input())
                        match Uinput:
                            case 1:
                                print("Oh yes! It's been hell on Earth for us ever since these monsters showed on up.")
                                print("We try to run them off, but they come in great numebers. It doesn't help that they come after dusk too.")
                                print("We're scared for our lives. They know our food's a target, and they're a very relentless mob indeed.")
                                print("*He leans on his pitchfork heavily")
                                print("---------------------------------------------------------------------------------------------")
                                case1 = False
                                tree1Sec1 = True
                            case 2:
                                print("Most of them are still at the farm working. I'm here because I was set on the lookout.")
                                print("The last attack was the worst we ever got it. We have to spread ourselves thin to")
                                print("make up for the lost men.")
                                print("---------------------------------------------------------------------------------------------")

                            case 3:
                                tree1 = True
                                tree11 = True
                            case 4:
                                if tree1Sec1 == True:
                                    print("It was terrible. About 13 were lost during the attack, including a mother and father.")
                                    print("People are sick with grief. I wish I could do more to help them. I really do.")
                                    
                case 2:
                    print("You can rest at the inn just a little further in. It says Catcher Sam's at the top. Couldn't miss it.")
                    portNo = False
                    tree1 = True  
                case 3:
                    print("That's right. They're knights sent straight from the baron, so they're the best we're going to have it.")
                    print("Their captain was named Hannibal. I think he's somewhere in the town.")
                    print("You won't find many though. I heared they were hurt really bad since their last adventure in that cave.")
                    print("May God rest their souls.")
                    portNo = False
                    tree1 = True            
                case 4: #case4
                    tree1 = False
                    tree11 = False
                    if case4 == True:
                        print("Well, there's a lot I could say. Depends on what you want to know!")
                        print("---------------------------------------------------------------------------------------------")
                    elif case4 == False:
                        print("*Fernando leans on his pitchfork")
                        print("---------------------------------------------------------------------------------------------")
                    else:
                        tree1 = True
                    #Responses
                    while not tree11:
                        print("---------------------------------------------------------------------------------------------")
                        print('(1) "Where can I buy armor and weapons?"')
                        print('(2) "Where can I buy healing items?"')
                        print('(3) "why is this place named Dandelion?"')
                        print("(4) Back")
                        Uinput = float(input())
                        match Uinput:
                            case 1:
                                print("From the square there should be a large grey buidling with shingles on the side.")
                                print("Just walk into the dullest building you see and you'll probably find it.")
                                print("It's ran by Andre. Great guy. He sells most of the wares we have available.")
                            case 2:
                                print("Oh yeah... I haven't been there in ages. I can't exactly remember.")
                                print("Try asking Andre, he's the main shopkeeper around here.")
                            case 3:
                                print("It means 'lion's tooth.' Natives of this land used to trade accessories made")
                                print("out of teeth of mighty cats, many of which were lions.")
                                print("Our village used to be a trading post for such items. Eventually, we became a town.")
                            case 4:
                                tree1 = True
                                tree11 = True
                case 5:
                    print('"AAAAAAAH"')
                    condition = True
                    #Adding combat code later. Hoping Pablo cooks fr.
                case 6:
                    condition = True
