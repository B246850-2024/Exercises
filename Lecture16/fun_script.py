#!/usr/bin/python

import time

details = {}

print("Hi,I will ask you a series of questions, and them comment on them. So bear with me for a few seconds.")

details["Name"] = input("\nFirst of all, what is your name?\n")

details["Age"] = input("\nHow many springs have your eyes witnessed?\n")

details["Colour"] = input("\nWhat is your favourite colour?\n")

details["Python"] = input("\nDo you like Python?\n")

details["World"] = input("\nThe world is flat: True or False?\n")


def funfunction(Name, Age, Colour, Python, World):
    print("\nNice to meet you", Name,". I am the Blind Seer.")
    time.sleep(3)
    
    if Age.isnumeric():
        Age = int(Age)
        print("\nUhmm... So this is your age...")
        time.sleep(5)
    
        print("\nThere is something crossing the veil towards me...")
        time.sleep(3)
    
        if Age < 3 or Age > 99 :
            print("\nYour age tells me the beginning and the end are one and the same.")
        else:
            print("\nYou have now lived", Age, "years.", "But your life too shall end one day...")
        time.sleep(7)
    else :
        print("What do you mean your age is", Age, "?")
        time.sleep(2)
        print("I cannot divine with non-numeric ages... This should be obvious...")
        return()

    print("\nSo your most beloved colour is", Colour.lower(), ". This does tell a lot about you.")
    time.sleep(3)
    
    print("\nHumm... There is something around you of that same colour...")
    time.sleep(3)
    
    print("\n Ah... Of course... It's your aura. Let me see it more carefully.")
    time.sleep(5)
    if Colour.upper() == "BLACK":
        print("\nA black aura... that is no good. I am sorry, but your final time draws near.")
    elif Colour.upper() == "WHITE":
        print("\nA white aura... that is briliant. You have a future of peace and enlightment ahead of you.")
    elif Colour.upper() == "BLUE":
        print("\nA blue aura... that is interesting. You will go through a revelation next time you are close to the sea")
    elif Colour.upper() == "YELLOW":
        print("\n An yellow aura... You will become a great artist, this tells me.")
    elif Colour.upper() == "RED":
        print("\n A red aura... This is curious. For some reason I cannot divine on this...")
    elif Colour.upper() == "GREEN":
        print("\n A green aura... You should go to the nearest forest and seek advice from the druid that lives there.")
    elif Colour.upper() == "PURPLE":
        print("\n A purple aura... That is most extraordinary. This means you too have an afinity with Divination.")
    else:
        print("\nA", Colour.lower(), "aura. That signifies a long, tranforming journey is ahead of you...")
    time.sleep(5)

    if Python.upper() in ["Y", "YES", "TRUE", "T"]:
        print("\nIt doesn't matter whether you like Python or not. This is not relevant to our Divination.")
    elif Python.upper() in ["N", "NO", "FALSE", "F"]:
        print("\nFear of snakes and/or coding languages signifies great pain coming rapidly towards you.")
    else:
        print("\nYour answer to the Python question \"", Python, "\"seems innapropriate.")
        print("\nThis should be a simple question, just answer yes or no. Seeing the future requires reliable information.")
        return()

    time.sleep(5)
    if World.upper() in ["Y" or "T" or "TRUE" or "YES"]:
        print("\nSo you believe the Earth is flat...")
        time.sleep(3)
        print("\n I see in the lines of destiny this belief will bring your ultimate destruction.")
    elif World.upper() in ["N", "NO", "FALSE", "F"]:
        print("\nSo you believe the Earth is round.")
        time.sleep(3)
        print("\nThis tells me that...")
        time.sleep(3)
        print("\nI see here in my crystal ball.")
        time.sleep(3)
        print("\nThat you are not stupid.")
    else:
        n = 1+1
    
    time.sleep(5)

    an = input("\nWere all you questions answered?\n")


    print("\nI knew you were going to say that, I see the future after all.")
    time.sleep(5)
    print("\nCome back after a full Moon cycle for more Divination. I must know silence...")
    time.sleep(2)
    print("\n Farewell,", Name)




funfunction(*list(details.values()))
