
##The comma at the end of the print line is so that print won't end with a newline, this will allow you to append a new print to the end of the line.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you are %r old, %r tall and %r heavy." %(age, height, weight)

#Taking the program further. Added this extra question and If statement for fun.
print "Is that correct?"
reply = raw_input()

if reply == 'Y':
    print 'Thank you'
else:
    print 'Ah well, I Tried'
