print("""you enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door=="1":
    print("There's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. Take the cake.")
    print ("2. Scream at the bear.")
    
    bear=input(">")
    
    if bear =="1" :
        print("The bear attacks you.(stupid)")
    elif bear=="2":
        print("This bear eats your leg.(Congradualtions moron)")
    else:
        print(f"Well doing {bear} is probably better.")
        print("Bear runs away")
    
elif door=="2":
    bear=input(">")
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow Jacket clothespins.")
    print("3. Understanding revovlers yelling melodies")
    print("4. Go off of instinct")
    if input=="4":
        print("You punch Cthulhu's retina... nothing happens and you walk to the door on the left")

insanity = input(">")