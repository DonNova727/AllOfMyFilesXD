The_placement = ['First place goes to','2nd place goes to','3rd place goes to','4th place goes to','5th place goes to','6th place goes to']
animals = ['bear','python','peacock','kangaroo', 'whale','platypus']
print("Do you want to see the results of the crazy animal race")
race = input(">")
if race == "yes":
    print("sure no prob.") 
print("which place are you curious about \n 1st 2nd 3rd 4th 5th or 6th")
race = input(">")
if race == "1st":
    animals = animals[0]
    placement= The_placement[0]
    print(f"{placement} the benveolent {animals}")
if race == "no":
    print("Fine, you'll never be able to forget a thing like that")
race = input(">")
if race == "2nd":
    animals = animals[1]
    placement = The_placement[1]
    print(f"{placement} the perfect {animals}")
race = input(">")
if race == "3rd":
    
    animals = animals[2]
    placement = The_placement[2]

