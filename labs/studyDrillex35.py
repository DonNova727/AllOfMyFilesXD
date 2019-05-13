from sys import argv

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice= input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else :
        
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print("nice your not greedy, you win")
        exit(0)
    else:
        dead("You greedy jerk the temples collapsing and you can't escape.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a buch of honey.")
    print("The fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input(">")
        
        if choice == "take honey":
            dead("The bear looks at you then slashes you with his claws")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear"  and bear_moved:
            dead("The bear gets pissed off and bites your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("print I got no idea what this means")
            
            
def cthulhu_room():
    print("Here you see the great evil cthulhu")
    print("He,it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input(">")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was... Disturbing that's... why in the world would you do.")
    else:
        cthulhu_room()
def dead(why):
    print(why,"good job!")
    exit(0)

def start():
    print("""You are in a dark room.
    There is a door to your right and left. 
    which on do you take?""")
    choice =input(">")
    
    if choice=="left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")
        
start()    