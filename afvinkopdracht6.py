import time
import re
'''
pos = 0
seq = "ATCGJ"
dnaBases = ["A", "C", "T", "G"]
isDNA = False

def recursiveDNA(seq, pos):
    print(pos)
    if pos > ( len(seq) - 1 ):
        isDNA = True
    currentBase = seq[pos]
    print(currentBase)
    if currentBase.upper() in dnaBases:
        isDNA = recursiveDNA(seq, pos+1)
    else:
        isDNA = False

    return isDNA
    '''
dnaBases = ["A", "C", "T", "G"]
pos = 0
seq = "ACTGJ"
isDNA = False
def recursiveDNA(seq, pos):
    if pos > ( len(seq) - 1 ):
        return True
    currentBase = seq[pos]
    if currentBase.upper() in dnaBases:
        isDNA = recursiveDNA(seq, pos + 1)
    else:
        isDNA = False

    return isDNA

def regexDNA():
    #Random sequentie genomen ipv het werkelijke p53 gen
    #NOTE| Deze functie wil op de een of andere manier alleen maar "None" printen, niet True of False
    #       ik weet niet hoe ik dat moet aanpassen
    # Probleem opgelost
    p53 = "^[ATCG]*$"
    seq = "ATCG"
    if bool(re.match(p53, seq)):
        return True
    elif not bool(re.match(p53, seq)):
        return False

def iteratieDNA():
    #Random sequentie genomen ipv het werkelijke p53 gen
    p53 = "ATCGGJ"
    g = p53.count("G")
    c = p53.count("C")
    a = p53.count("A")
    t = p53.count("T")
    if a + t + c + g == len(p53):
        return True
    elif a + t + c + g != len(p53):
        return False

def iteratief():
    #startTime = time.time()
    x = int(input("How many numbers do you want in the Fibonacci sequence? "))
    y = 0
    z = 1
    for i in range(x):
        print(y)
        y, z = z, y+z
    #endTime = time.time()
    #timer = endTime - startTime
    #print("The iterative function takes", timer, "milliseconds")


def GenerateFibonacci(i):
 if(i == 0):
  return 0

 elif(i == 1):
  return 1

 else:
  return GenerateFibonacci(i-1) + GenerateFibonacci(i-2)

def recursief():
    #startTime = time.time()
    x = int(input("How many numbers do you want in the Fibonacci sequence? "))
    for i in range(x):
        print(GenerateFibonacci(i))
    #endTime = time.time()
    #timer = endTime - startTime
    #print("The recursive function takes", timer, "milliseconds")
    
def main():
    x = input("Welke functie wil je uitvoeren? a = recursief, b = iteratief, c = iteratieDNA, d = regexDNA, e = recursieDNA ")
    startTime = time.time()
    if x == "a":
        recursief()
    if x == "b":
        iteratief()
    if x == "c":
        print(iteratieDNA())
    if x == "d":
        print(regexDNA())
    if x == "e":
        rec = recursiveDNA(seq, pos)
        print(rec)
    endTime = time.time()
    timer = endTime - startTime
    print("This took", timer, "milliseconds")




main()
