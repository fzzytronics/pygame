import time
import Monkey
import FernandoDialogue
from pysc import face
from pysc import village


firstScene = True
while firstScene:
    print("""It's a terrifying and unfamilar age.

        You're a warrior, battered and bruised from your latest campaign.
          You can barely stand on your feet.
           Your vision is blurry, and your head is pounding.

    Pick Your Options
    (1) Look At Yourself
    (2) Look At The Town
    (3) Check Your Stuff
    (4) Walk On""")

    Uinput = float(input())
    match Uinput:
        case 1:
            face.game()
            print("---------------------------------------------------------------------------------------------")
            print(""""Your face is twisted in a bizarre form of anguish.
The battle has taken its toll on you.""")
            print("---------------------------------------------------------------------------------------------")
        case 2:
            village.game()
            print("---------------------------------------------------------------------------------------------")
            print(""""A small town stands before you, a distance so close you could make it before your legs
fail you. The buildings hang low with flat, mahogany rooves. The white walls reflect the orange
rays of the setting sun on the dirt.""")
            print("---------------------------------------------------------------------------------------------")
        case 3:
            print("---------------------------------------------------------------------------------------------")
            with open("text/inv.txt", 'r') as file:
                content = file.read()
                print(content)
            print("---------------------------------------------------------------------------------------------")
        case 4:
            firstScene = False
