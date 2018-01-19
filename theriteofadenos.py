#Authors: Trevor Naughton, Austin Hinkel
#Date: 1/12/18
#Title: pythonGame.py

"""



████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗  
   ██║   ██╔══██║██╔══╝  
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝                     

██████╗ ██╗████████╗███████╗     ██████╗ ███████╗
██╔══██╗██║╚══██╔══╝██╔════╝    ██╔═══██╗██╔════╝
██████╔╝██║   ██║   █████╗      ██║   ██║█████╗  
██╔══██╗██║   ██║   ██╔══╝      ██║   ██║██╔══╝  
██║  ██║██║   ██║   ███████╗    ╚██████╔╝██║     
╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═╝                                                     

 █████╗ ██████╗ ███████╗███╗   ██╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔═══██╗██╔════╝
███████║██║  ██║█████╗  ██╔██╗ ██║██║   ██║███████╗
██╔══██║██║  ██║██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║  ██║██████╔╝███████╗██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                   
                                          
                          By
                    Trevor Naughton
                          &
                    Austin Hinkle

   
"""
print("The Rite of Adenos\n")
input("---Chapter 1---")
name = input("What is your name, brave soul? ")

input(name)
input(name + "...")
input(name + ", it is I, Adenos. A great evil is upon us and I cannot stop it alone. Sanavaur has released his agents of Kaliron to rid this world of good...Please help us." + "\n")

input("-----WAKE UP-----")

chapter1 = "Across a vast, arid desert, an illuminated obelisk appears. \n" + \
           "\t'Who enters my domain?' the looming tower rumbles.'"
print(chapter1)
ans = input("It is often our decisions and choices that will make us who we are in life, " + name + ". Type 1 for bravery, 2 for cowardice: ")

if ans == "1":
    print("\t'It is I, " + name + ", the brave and strong!'")
elif ans == "2":
        print("\tUh, it's...me" + name + "." + " *Shuffles feet awkwardly*")
else:
        print("\t...sand crickets chirp loudly...")

print("The ground erupts with the roar of the tower's laughter.")
print("\t'What is your quest, young " + name + "? Do you wish to defeat me?'")
print("\t'I can see that you are but a fledgling so I shall be merciful before your folly. I inhabit this vessel as Sanavaur of Kaliron. All know and fear my wrath.")

rebuttal = input("What will you say to this mocking fiend? Surely you will do something! Type 1 for bravery, 2 for cowardice: ")

if rebuttal == "1":
    print("\t'Snyde beast. Come down from your quarters and face me like the fiend you claim to be. I will twhwart your evil ways and rid you of this land.' said " + name + ".")
elif rebuttal == "2":
    print("\t'Understood. You would have bested me in any battle, I thank you for my life.' said " + name + ".")
else:
    print("...sand crickets chirp loudly...")
print("The sky darkens overhead and the dunes begin squirming underfoot.")
print("\t'Heed my lecture, mire-sucking ingrate. Trespass in my midst again and I will ensure your name will echo through time.'")
print("A pyre of flame screams from the heavens, barely missing your side!")

choice = input("You were nearly killed! Thank goodness the fireball missed you. Now you must choose to engage with the chance of dying or run with your life in tow. Choose 1 for bravery, 2 for cowardice.")

if choice == "1":
    print("\t'Is that all Sanavar can muster?' " + name + " said as he drew out his longsword.")
elif choice == "2":
    print("\t'I am sorry to have disturbed you Sanavar. Please have mercy on me.' " + name + " said as he ran to the hills.")
else:
    print("'I have no quarrel with you.' You turn heel and leave the desert.")

print("'BURN!!!' Screamed Sanavar as another fireball engulfs you.")
print("You loose your footing and all turns dark.")

input("---Chapter 2---")
print("Your eyes open slowly them darting side to side you lift your head seeing a old hagg cleaning your feet.")
choice2 = input("Either 1:Kick her in the face. 2:Let it happen. or 3:Leave. ")
if choice2 == "1":
    print("You kick her in the face, she bolts back \n \t You dare kick me in the face ***she shrieks as she reaches for a knife*** you leap back \n disgusted and bolt out the door.")
elif choice2 == "2":
    print("Looking down at the old hagg you notice warts covering her face and her back looking jagged and deformed. You calmly ask what happened \n to you and why she is cleaning your feet. She responds with a grunt saying your feet are badly burned. She expresses that your wounds are \n healed and you must leave to complete your task for Adenos. As you stand the old hagg shoves you out of the hut and slamsmthe door.")
elif choice2 == "3":
    print("You pull your feet away getting off the straw bed you were laying on and walk out of the hut not saying a word.")
    
