#Kinda like scripts with argv
def print_two(*dogs):
    arg1, arg2 = dogs
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#that *args is pointless so lets do something different

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

#this takes one argument
def print_none():
    print "I got nothin'."

print_two("Arshad", "Umrethi")
print_two_again("Arshad", "Umrethi")
print_one("Uno!")
print_none()
