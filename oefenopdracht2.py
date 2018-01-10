




i = 1




def multiply(x, y, i):
    x1 = x
    while i < y:
        #print(x)
        x += x1
        i += 1
    if not i < y:
        return x
    multiply(x, y, i)






def main():
    x = int(input("Please add a number you want to have multiplied: "))
    y = int(input("Please add a number you want to multiply by: "))
    answer = multiply(x, y, i)
    print(answer)


main()
