from math import *
import Harold_Mad
# Dialogue 
secretHarold1 = False #This will turn to true if the correct dialogue option is chosen 
def game():
    print('My name is Harold. Hello.')
    class Harold:
        condition = False
        while not condition: #Repeats when wrong key is pressed. Proceeds when correct keys are typed
            print('░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░░░')
            print('░░░░░░░░░▄▄█████████████▄░░░░░░░░░░░░░░░')
            print('░░░░░░░▄██████████████████░░░░░░░░░░░░░░')
            print('░░░░░▄██████████████▀▀▀░▀██░░░░░░░░░░░░░')
            print('░░░░▄██████▀▀▀▀▀▀░░░░░░░░▀██░░░░░░░░░░░░')
            print('░░░░████████░░░░░░░░░░░░░░▀█░░░░░░░░░░░░')
            print('░░░░████████░░░░░░░░░░░░░░▄█▄░░░░░░░░░░░')
            print('░░░░████████░░░░░░░░░░▄░░███▀░░░░░░░░░░░')
            print('░░░░░██████░░░░░█▀███▀▀░░░░░░░░░░░░░░░░░')
            print('░░░░░███████░░░░░▀▀▀░░░░░░░░░░░░░░░░░░░░')
            print('░░░░░▀█░░▀██░░░░░░░░░░▄░░░░▀░░░░░░░░░░░░')
            print('░░░░░░▀▄░░▄▀░░░░░░░░░░░▄████▀░░░░░░░░░░░')
            print('░░░░░░░░░░░░▄░░░░░░░░██▀█▄██░░░░░░░░░░░░')
            print('░░░░░░░░░░░▀░░░░░░░░░░░▀▀▀▀▀░▀░░░░░░░░░░')
            print('░░░░░░▄▄▄███░░░░░░░░░░░░░░░░░█▄░░░░░░░░░')
            print('▄▄▄█████████▀░░░░░░░░▄▄░░░░▄▄█████▄▄▄░░░')
            print('████████████░░░░░░░░░░██████████████████')
            print('█████████████░░░▀░░░░░▄█████████████████')
            print('██████████████░░░▄█▀▀█▀▀████████████████')
            print('(1) "What do you do?"')
            print('(2) "Why is your name Harold?"')
            print('(3) Fight Harold')
            print('(4) Leave')
            if secretHarold1 == True:
                print('(5) I like cooks. Travel with me')
            Uinput = float(input())
            match Uinput: #Dialogue tree
                case 1:
                    print('I cook.')
                    print('(1) Why do you cook?')
                    print('(2) I think your cooking is dumb')
                    Uinput = float(input())
                    match Uinput:
                        case 1: 
                            print('Because I enjoy it')
                            secretHarold1 = True
                        case 2:
                            print('You are human trash')
                        case 3:
                            print('Please Type A Valid Number')
                case 2:
                    print('Because I like the sound of it.')
                case 3:
                    print('AAAAAAAAA')
                    Harold_Mad.game()
                    break
                case 4:
                    condition = True
                case 5: #Secret Option Unlocked
                    if secretHarold1 == True:
                        print('Sure!')
                        condition = True
                case _:
                    print('Please Type A Valid Number')
