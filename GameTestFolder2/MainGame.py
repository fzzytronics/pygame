import HaroldTest
import FernandoDialogue
from pysc import face
from pysc import village
with open(r"C:\Users\jaedyn mcneil\OneDrive\Desktop\pygame-main\GameTestFolder\text\death.txt", "w") as file: #clears file
        file.writelines("")
def game():
    firstScene = True
    townScene2 = True
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
    fail you. The buildings hang low with flat, mahogany rooves. The white walls reflect the warm, cascading
    rays of the setting sun on the dirt.""")
                print("---------------------------------------------------------------------------------------------")
            case 3:
                print("---------------------------------------------------------------------------------------------")
                with open(r"C:\Users\jaedyn mcneil\OneDrive\Desktop\pygame-main\GameTestFolder\text\inv.txt", 'r') as file: #where the items are
                    content = file.read()
                    print(content)
                print("---------------------------------------------------------------------------------------------")
            case 4:
                firstScene = False
                townScene2 = False
                townScene = True
            case _:
                print("---------------------------------------------------------------------------------------------")
                print("Enter Valid Input")
                print("---------------------------------------------------------------------------------------------")
  
    while townScene2:
        print("---------------------------------------------------------------------------------------------")
        print("""Fernando's body lies in the dirt. 
    (1) Head to the houses.
    (2) Head to the town.""")
        Uinput = float(input())
        match Uinput:
            case 1:
                print("New npc coming soon :( )")
            case 2:
                townScene2 = False
            case _:
                print("Invalid input.")



    while townScene:
        print("---------------------------------------------------------------------------------------------")
        print("""You take the dirt path to the town. In front of you are a handful of houses, a fenced off farm,
    And the main path. 

    (1) Head to the farm.
    (2) Head to the houses.
    (3) Head to the town.""")
        Uinput = float(input())
        match Uinput:
            case 1:
                FernandoDialogue.fernando()
                with open(r"C:\Users\jaedyn mcneil\OneDrive\Desktop\pygame-main\GameTestFolder\text\death.txt", 'r') as file:
                        for x in file:
                            if x.strip() == "yes":
                                print("You Died")
                                townScene = False
                                break
                            elif x.strip() == "no":
                                townScene2 = True
                                townScene = False
            case 2:
                HaroldTest.game()
                townScene = False
            case 3:
                townScene = False
            case _:
                print("Invalid input.")