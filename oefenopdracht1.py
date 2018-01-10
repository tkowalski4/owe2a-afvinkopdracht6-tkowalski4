



i = 0


'''def printer(n, i):
    while n >= i:
        print(i)
        i += 1
        if i > n:
    printer(n, i)
'''

'''def printer(n, i):
    if n >= i:
        printer(n, i - 1)
        print(i)
        '''

def printer(n, i):
    print(i)
    if i < n:
        printer(n, i + 1)


def main():
    n = int(input("Please enter a random number: "))
    printer(n, i)




    

main() 
