from sys import argv

#takes in input from the command line
script, filename = argv

#opens the file specified from command line argument in read only mode
txt = open(filename)

#reads in whatever is in the file 
print ("The file you opened is %r" % filename)
print (txt.read())

txt.close()

print ("Would you like to add something to the file?")
print ("If yes, press 'y'. If not, press 'n'")

decision = input()

if(decision == 'y'):
    #opens the file in append mode. Will write to next line when using write function.
    txtw = open(filename, 'a')
    print("Start typing what you would like to add to the file. Hit enter when you are done.")

    addition = input()

    #writes to the file
    txtw.write(addition)
    txtw.write("\n")
    txtw.close()

    print("Your message has been added!")
else:
    print("Thank You!")



