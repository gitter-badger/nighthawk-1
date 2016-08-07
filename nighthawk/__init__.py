# NIGHTHAWK 2016 (C)
# AL3X V3GAS 2016 (C)
# THE AVX PROJECT 2016 (C)
# NIGHTHAWK 2016.1.0 NOX

import os # imports the inbuilt OS module
import shutil # imports the inbuilt SHUTIl module
import random # imports the inbuilt RANDOM module

# This is the listing function developed by AL3X V3GAS.
# This function uses some utilities from the OS module.
# The function name 'lc' stands for 'list contents'.
# The function is similar to the 'ls'  command in Linux
# or the 'dir' command in Windows. Number of args: 0
def lc():
    workingdir = os.getcwd()
    contents = os.listdir(workingdir)
    icount = len(contents)
    icountloop = int(icount) + 1
    for i in range(0, icount):
        item = contents[i]
        print (" " + str(item))

# This function simply makes a file with the file name
# the user specifies. This command is similar to the 'touch'
# command in Linux. Number of args: 1
def mkf(fname):
    file = open(fname, "w")
    file.close()

# This function simply makes a file with the directory name
# the user specifies. This command is similar to the 'mkdir'
# command in Linux or the same command in Windows. The name 'mkfs'
# stands for 'make file system'. Number of args: 1
def mkfs(dirname):
    os.makedirs(dirname)

# This function writes to an existing file that can be read as a text file.
# The argument name 'fname' stands for 'filename' and the function name
# 'stringwrite' stands for 'string to write'. Number of args: 2
def mkc(fname, stringwrite):
    strfname = str(fname)
    strstringwrite = str(stringwrite)
    print ("Checking if the file '" + strfname + "' exists.")
    if os.path.isfile(strfname) == False:
        print ("File not found.")
        print ("Nonexistent file cannot be written to.")
    if os.path.isfile(strfname) == True:
        print ("File has been found.")
        print ("Editing...")
        file = open(strfname,"a")
        file.write(strstringwrite)
        print ("..done.")

# This function deletes a file. Before this operation is attempted,
# the existence of the file is verified. If it is verified, then the
# operation is carried out without delay. Number of args: 1
def rmvf(filename):
    if os.path.isfile(filename) == True:
        print ("File existence verified, deleting...")
        os.remove(filename)
        print ("File deleted!")
    else:
        print ("File not found.")

# This function deletes a directory. Before this operation is attempted,
# the existence of the directory is verified. If it is verified, then the
# operation is carried out without delay. The contents of the
# the directory is also deleted. Number of args: 1
def rmvfs(dirname):
    if os.path.isdir(dirname) == True:
        print ("Directory existence verified, deleting...")
        shutil.rmtree(dirname)
        print ("Directory deleted!")
    if os.path.isfile(dirname) == False:
        print ("Directory not found.")

# This function renames a file. Before the file is renamed,
# it's existence is verified. If it is verified positively
# the file is renamed, if it is verified negatively the operation
# is not carried out and an error is returned.
def rnmf(orig_name, new_name):
    if os.path.isfile(orig_name) == True:
        return ("Directory found, renaming...")
        os.rename(orig_name, new_name)
    elif os.path.isfile(orig_name) == False:
        return ("The file '" + str(orig_name) + "' was not found.")

# This function generates a key code with the following format:
# KEY CODE FORMAT:
# * LETTER-NUMBER-LETTER-NUMBER
# * The numbers can have up to 9 digits.
# * The maximum length of the key code can be up to 20 places.
def keygen_main():
    rp1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a = -1000000000
    b = 1000000000
    code1 = random.randint(a,b)
    code2 = random.randint(a,b)
    let1 = random.choice(rp1)
    let2 = random.choice(rp1)
    codef = str(let1) + str(code1) + str(let2) + str(code2)
    return codef

# This function generates a key code with the following format:
# KEY CODE FORMAT:
# * LETTER-NUMBER-LETTER-NUMBER
# * The key code has a length of 4 places.
def keygen_small():
    rp1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rp2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
    let1 = random.choice(rp1)
    let2 = random.choice(rp1)
    num1 = random.choice(rp2)
    num2 = random.choice(rp2)
    code = str(let1) + str(num1) + str(let2) + str(num2)
    return code

# This function determines whether the function
# that has been put in by the user is an integer.
# If it is an integer, then the output states 'True',
# if not, then the output states 'NaN'.
def isNumber(a):
    while True:
        try:
            return int(a)
            break
        except ValueError:
            return 'NaN'

# This function finds out all the the prime factors
# of the user argument. This function is then processed
# further by prime(arg).
def factors(n):
    _list = []
    for a in range(1, int(n)+1):
        if n % a == 0:
            _list.append(a)
    return _list

# This function finds out whether the number that the user
# has put in, is a prime number. This function will work admirably
# for smaller numbers. Bigger numbers starting from 1 * 10 ** 6
# will take more time to analyze.
def prime(a):
    factor_list = factors(a)
    factor_length = len(factor_list)
    if a in factor_list and 1 in factor_list and factor_length == 2:
        return True
    else:
        return False

# This function adds two numbers with two floating point numbers.
def addition(b,c):
    addition = (float(b)+float(c))
    return addition

# This function subtracts two numbers with two floating point numbers.
def subtraction(b,c):
    subtraction = (float(b)-float(c))
    return subtraction

# This function multiplies two numbers with two floating point numbers.
def multiplication(b,c):
    multiplication = (float(b)*float(c))
    return multiplication

# This function divides two numbers with two floating point numbers.
def division(b,c):
    division = (float(b)/float(c))
    return division

# This function converts a given value in degrees
# Fahrenheit into its corresponding Celsius value.
# This function deals with temperature only.
def celsius(f):
    celsius = (float((float(5)/float(9)) * float(float(f) - 32)))
    return celsius

# This function converts a given value in degrees
# Celsius into its corresponding Fahrenheit value.
# This function deals with temperature only.
def fahrenheit(g):
    fahrenheit = (float(float(g)/float(float(5)/float(9))) + float(32))
    return fahrenheit

# This function calculates the velocity it has taken
# a body to move a certain distance in a certain time.
def velocity(i,j):
    velocity = (float(i)/float(j))
    return velocity

# This function calculates the distance it has taken a body
# to move at a certain constant velocity in a given time.
def distance(k,l):
    distance = (float(k) * float(l))
    return distance

# This function calculates the time it has taken a body
# to move at a certain constant velocity for a given distance.
def time(m,n):
    time = (float(m)/float(n))
    return time

# Let a be a given number. If the user types another number b,
# loopmultiplier(arg1, arg2) will multiply a with b starting
# with a times 1 until it iterates through to b.
def loopmultiplier(o,q):
     w = 1 + int(q)
     j = 0
     for j in range(1,int(w)):
         value = (str(float(o)) + (" x ") + str(float(j)) + (" = ") + str(float(o)*float(j)))
         print (str(value))
     return value

# This function determines the end value of
# an expression only containing integers.
def expro(a):
    exval = eval(str(a))
    return exval

# This function determines the number of seconds in a lightyear.
def lightyear():
    ly = str(60 * 60 * 24 * 365 * 2.99 * 10 ** 9)
    return ly

# This function determines the factorial of an integer.
def fact(num):
    iter_int = int(int(num) + 1)
    factorial = 1
    for i in range(1,iter_int):
        factorial = factorial * i
    return factorial

# This function returns the binomialcoefficient for
# two given values n and k. N represents the whole,
# K represents the part.
def bnmcoef(n,k):
    n_fact = float(fact(n))
    k_fact = float(fact(k))
    dif_nk = float(n) - float(k)
    result = float(n_fact/(dif_nk * k_fact))
    return result
