#If- else statements
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a chocolate cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    alt = "1 or 2"

    if bear == "1":
        print "The bear eats your face off Good Job!"
    elif bear == "2":
        print "The bear eats your lefs off, Good Job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % alt

elif door == "2":
    print "You stare into the abyss inside Chtulhu's eye"
    print "1. Blueberries"
    print "2. Yellow jacket potatoes"
    print "3. Understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or "2":
        print "Your body survives powered by a mind of jello. Good Job!"
    else:
        print "The insanity rots your eyes into a dark pool of muck. Good Job!"

else:
    print "You stumble around and fall on a knife and die. Good Job!"
