# AL3X V3GAS 2016 (C)
# PWDGEN-NIGHTHAWK 2016 (C)
# THE AVX PROJECT 2016 (C)

import os # OS utilities
import nighthawk # imports nighthawk

file = open("log.txt", "w") # makes a log file with write permission
file = open("log.txt", "a") # changes the permission to writing into the file


def isintnum(num): # function to determine whether the user argument is a number
    while True:
        try:
            return int(num)
            break
        except ValueError:
            return 'NaN'

print ("")
print ("PWDGEN Console 1.0")
print ("Type 'help' to view a list of commands!") # console preamble
a = "pwdgen" # initialize variable
location = os.getcwd()
while a != "exit" and a != "exit()": # define exceptions
    a = input("pwdgen@console=>" + str(location) + ">> ") # ask for input
    if a == "license": # display license agreement
        print ("")
        print ("This software is licensed under the GNU GPL v3.0!")
        print ("")

    if a == "help": # display help message
        print ("")
        print (" help       display this")
        print ("")
        print (" license    license agreement")
        print ("")
        print (" generate   generate values")
        print ("")
        print (" exit       exits shell")
        print ("")

    if a == "generate": # generate password
        b = "pwdgen" # initialize variable
        while (isintnum(b) == "NaN") == True:
            b = input("Type the number of key codes here: ") # ask for input
            if (isintnum(b) == "NaN") == True:
                print ("")
                print ("Inavlid argument!")
                print ("Try again!")
                print ("")
        rng = int(b) + 1
        for i in range(1,rng):
            print (str(nighthawk.keygen_small())) # display key code
            file.write(str(nighthawk.keygen_small()) + "\n")
        file.close()
        print ("")

    if a == "": # for no input
        pass

    if a == "exit" or a == "exit()": # in case the user wishes to quit the console
        exit()

    if a != "exit" and a != "exit()" and a != "license" and a != "help" and a != "generate": # error handling
        print ("")
        print ("Invalid Input!")
        print ("")
