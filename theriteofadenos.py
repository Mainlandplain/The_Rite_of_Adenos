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
    
ap = input("*You see a traveler walking toward you* \n (1) Stop the traveler and ask him why he is walking away from town \n (2) Keep walking \n")
if ap == "1":
    ab = input("Sir, why is it you are leaving the town.  *The man replies to your question with a confusing look* \n Because it's in the path of the demons so I thought to get as far away from here as possible. \n (1) Ask about the demons. \n (2) Be on your way.\n")
    if ab == "1":
        print("Wait, did you just say there are demons? \n *Man replies* Yes where have you been the past couple weeks.")
    elif ab == "2":
        print("Well have safe travels.")
elif ap == "2":
    ac = input("You continue on ignoring the traveling man. *As you're walking past him he grabs your arm* \n *The man says* Do you have a death wish or something?\n (1) Shove him off you.\n (2) Ask what hes talking about. \n")
    if ac == "1":
        from random import *
        x = int(randint(1, 20))
        print(x)
        if x in (1, 2, 3, 4, 5) :
            print("*You push him off you, while you do so you lose your footing and fall to the ground*")
        elif x in (6, 7, 8, 9, 10) :
            print("*You are barely able to shove him off you making you look as weak as a newly born child*")
        elif x in (11, 12, 13, 14, 15) :
            print("*You successfully push him off you*")
        elif x in (16, 17, 18, 19) :
            print("*You throw him off you with pushing him onto the ground*")
        elif x in (20, 21) :
            print("*Critical hit*")
            from random import *
            b = int(randint(1,20))
            print (b)
            if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
                print("*You throw him off of you with such force he breaks his arm on the fall*") 
            elif b in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20) :
                print("*You throw him off you with a god like strength, he flys back and his neck snaps like a twig when he hits the ground*")
    elif ac == "2":
        print("What are you talking about. \n *man replies* There are demons in that direction")
print("*You continue on down the path toward the town*")
watchout = input("*As you aproach the town you get stopped by a raggity looking man* \n -Highwayman- Where do you think you're going pip-squeak. \n *He shoves you back* Wheres your money. \n (1) I don't have any money. \n (2) Shove him back. \n (3) Draw your sword. \n ")
if watchout == "1":
    stance = input("I don't have any money. \n -Highwayman- Give me your money or I will gut you like a pig. *He pulls out a rusty knife* \n (1) I really don't have any money. \n (2) Draw out your sword. \n ")
    if stance == "1":
        print("*You turn out your pockets* See I don't have anything. \n -Highwayman- *The man grunts* Fine you can leave, but if I see you again I will gut you.")
    elif stance == "2":
        print("*You go to draw your blade*")
        from random import *
        x = int(randint(1, 20))
        print(x)
        if x in (1, 2, 3, 4, 5) :
            print("*You fail at drawing your sword fast enough and get stabbed by the highwaymans rusty dagger*")
        elif x in (6, 7, 8, 9, 10) :
            print("*You are able to draw your sword and deflect the highwaymans dagger*")
        elif x in (11, 12, 13, 14, 15) :
            print("*You draw your sword deflecting the highwaymans attack and slicing his face in the process*")
        elif x in (16, 17, 18, 19) :
            print("*You draw your sword and quickly deflect his rusty dagger then thrusting your sword in his chest killing him*")
        elif x in (20, 21) :
            print("*Critical Hit")
            from random import *
            b = int(randint(1,20))
            print (b)
            if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
                print("*Drawing your sword with the speed of the gods you cleave the highwaymans head clean off before he could even react*") 
            elif b in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20) :
                print("*You draw your sword sa fast the highwayman has no time to react, it almost seems as if time has slowed at your whim* \n *You cut off his hand holding the dagger and as he screams you cut off his head with one swift movement*")
elif watchout == "2":
    from random import *
    x = int(randint(1, 20))
    print(x)
    if x in (1, 2, 3, 4, 5) :
        print("*You are unable to shove him off of you* \n -Highwayman- *He laughs at your attempt* You think you can get away. *He pulls out a rusty dagger*")
        sworda = input("(1) Draw your sword \n ")
        from random import *
        x = int(randint(1, 20))
        print(x)
        if x in (1, 2, 3, 4, 5) :
            print("*You draw your sword barley able to deflect his dagger*")
        elif x in (6, 7, 8, 9, 10) :
            print("*You draw your sword and deflect his attack and also slicing his cheek in the process*")
        elif x in (11, 12, 13, 14, 15) :
            print("*You kick him back as you draw your sword from its sheath \n after kicking him back he falls to the ground and you rush him holding your blade to his neck*")
        elif x in (16, 17, 18, 19) :
            print("*You draw your sword with great speed and thrust it into his cheast before he can react*")
        elif x in (20, 21) :
            print("Critical Hit")
            from random import *
            b = int(randint(1,20))
            print (b)
            if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
                print("*You draw your sword deflecting the attack and in one fatial strike you behead the Highwayman*") 
            elif b in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20) :
                print("*As you draw your sword a bolt of lightening shoots from the sky turning the man into ash*")
    elif x in (6, 7, 8, 9, 10) :
        print("*You shove him off of you* \n -Highwayman- *He takes a step back and pulls out a rusty dagger* ha! This will be fun.")
        from random import *
        x = int(randint(1, 20))
        print(x)
        if x in (1, 2, 3, 4, 5) :
            print("*You disarm the man knocking his dagger to the ground* \n *The Highwayman runs away afraid what you might do to him*")
        elif x in (6, 7, 8, 9, 10) :
            print("*You quickly draw your sword before he can attack you, you slice at his chest wounding him* \n *He runs into the woods wounded trying not to bleed out in the process*")
        elif x in (11, 12, 13, 14, 15) :
            print("*You draw your sword and with one sweeping motion you cut off the Highwaymans hand* \n *The Highwayman runs off stumbling into the woods*")
        elif x in (16, 17, 18, 19) :
            print("*You draw your sword out of its sheath as you do this its as if time has slowed giving you more than enough time to win the fight* \n *You cut off the Highwaymans hand and do a spinning swing beheading the man with one swing*")
        elif x in (20) :
            print("Critical Hit")
            from random import *
            b = int(randint(1,20))
            print (b)
            if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
                print("*As you draw your blade the man is rammed by a ox* \n *Horns plungged into the Highwayman as the ox runs by taking the man piked on his head with him*") 
            elif b in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20) :
                print("*Before you even have the chance to draw your sword the Highwayman starts to thrust his dagger at you* \n *Before the blade even touches you a lightening bolt comes from the sky killing him instantly*")
    elif x in (11, 12, 13, 14, 15) :
        print("*You push him off of you throwing him back a few steps* \n -Highwayman- *He stands back* Look man I didn't mean anything by it it's just hard you can go on your way.")
    elif x in (16, 17, 18, 19) :
        print("*You throw him off you like hes nothing pushing him to the ground* \n -Highwayman- *He quickly stands up and runs for the woods*")
    elif x in (20, 21) :
        print("Critical Hit")
        from random import *
        b = int(randint(1,20))
        print (b)
        if b in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
            print("*You flick him off you likes hes but only an annoying bug* -Highwayman- *He stumbles off back into the woods*") 
        elif b in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20) :
            print("*You shove him off you throwing him several feet, not realizing your own strength you see he had cracked his head open* \n ==The Highwayman was dead==")
elif watchout == "3":
    print("*You pull out your sword as you do the Highwayman stumbles back afraid and runs off into the woods*")

    
