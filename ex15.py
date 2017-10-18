from sys import argv

# #argv pass arguments into the program call
# script, filename = argv
#
# #assign the open function with filename argument to txt variable
# txt = open(filename)
#
# #Description of the file is printed before the file itself.
# print "Here's your file %r:" % filename
#
# #Used the .read method to read the variable txt in
# print txt.read()
#
# #The same thing is repeated this time with different approach
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
