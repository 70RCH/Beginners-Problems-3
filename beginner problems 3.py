#starter
height = int(input("How tall are you?"))
if height > 120:
    print ("You can ride the roller coaster!")
else:
    print ("Sorry. You can’t ride the rollercoaster!")

#Choose your own adventure!
def start():
 print ("You are exploring a rain forest in search of treasure. Legend has it that there are some buried on a nearby island.")
 ans1 = input ("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait):")
 if ans1 == ("wait"):
    print ("You are saved by a boat. Next one.")
 elif ans1 == ("swim"):
    print ("You get eaten by a hungry shark. Game over. ")
    return
 else:
    print ("Why don't you listen to the instruction??? Game over.")
    return
 ans2 = input ("There is a dumpling. Do you want to eat that? (eat/not eat):")
 if ans2 == ("eat"):
    print ("What a yummy dumpling! Next one.")
 elif ans2 == ("not eat"):
    print ("You starve to death. Game over.")
    return
 else:
    print ("Why don't you listen to the instruction??? Game over.")
    return
 ans3 = input ("There are three ways. The map says go along the middle one. Which one do you want to go? (left/middle/right):")
 if ans3 == ("middle"):
    print ("Good guy. You find the treasure and win!")
 elif ans3 == ("left"):
    print ("You become a shark and can only eat swimming people. Game over.")
 elif ans3 == ("right"):
    print ("You become a dumpling and can only be eaten. Game over.")
 else:
    print ("Why don't you listen to the instruction??? Game over.")
start()
