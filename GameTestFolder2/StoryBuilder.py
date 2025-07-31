from ollama import chat
import random
import openScene

def game():
    fileWipe = r"C:\Users\jaedyn mcneil\OneDrive\Desktop\pygame-main\GameTestFolder\text\inv.txt"
    f = open(fileWipe, "w")
    f.close()

    itemList = []

    print("""If you were in the Middle Ages, what would your class be? (Type answers below verbatim)
    Soldier
    Thief
    Missionary
    """)
    Status = input() #Type class to obtain weapon
    match Status:
        case "Soldier":
            classChoose = "soldier"
            weaponChoose = "longsword\n"
        case "Thief":
            classChoose = "theif"
            weaponChoose = "dagger\n"
        case "Missionary":
            classChoose = "missionary"
            weaponChoose = "staff\n"
        case _:
            print("You didn't type it right, we're just going to give you soldier.")
            classChoose = "soldier"
            weaponChoose = "longsword\n"

    itemList.append(weaponChoose)
    print("-") #triggers randomizer that chooses two new times
    print("Is your past tragic? // Type YES or NO")
    Status = input()
    match Status:
        case "YES":
            pastTrag = "tragic"
            for _ in range(2):
                num = random.randrange(1,5)
                match num:
                    case 1: 
                        item1 = "flask\n"
                    case 2:
                        item1 = "firebomb\n"
                    case 3:
                        item1 = "crowbar\n"
                    case 4:
                        item1 = "greatcoat\n"
                    case 5:
                        item1 = "leathergloves\n"
                itemList.append(item1)


        case "NO":
            pastTrag = "good"
            for _ in range(2):
                num = random.randrange(1,5)
                match num:
                    case 1: 
                        item1 = "flask\n"
                    case 2:
                        item1 = "bowgun\n"
                    case 3:
                        item1 = "jackknife\n"
                    case 4:
                        item1 = "greathelm\n"
                    case 5:
                        item1 = "leatherboots\n"
                itemList.append(item1)
        case _:
            print("YES or NO, can't be that hard. Forget it, you're getting a tragic backstory. Dumbass.")
            pastTrag = "tragic"
            for _ in range(2):
                num = random.randrange(1,5)
                match num:
                    case 1: 
                        item1 = "flask\n"
                    case 2:
                        item1 = "firebomb\n"
                    case 3:
                        item1 = "crowbar\n"
                    case 4:
                        item1 = "greatcoat\n"
                    case 5:
                        item1 = "leathergloves\n"
                itemList.append(item1)

    #Reading the inventory
    with open(fileWipe, "w") as file:
        file.writelines(itemList)
    inventory = "text/inv.txt"  # Replace with the actual path to your file



    messages = [
    {
    'role': 'user',
    'content': 'Type a 2 sentence backstory for a medieval '+classChoose+'that has a .'+pastTrag+'backstory.',
    },
    ]
    for part in chat('llama3.2', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)

    con = True
    print(" Time to start... press y")
    
    while con:
        Uinput = input()
        if Uinput == "y":
            con = False
            openScene.game()
        else:
            print("Just start the game dude.")