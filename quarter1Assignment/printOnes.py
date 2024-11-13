def printOnes(num):
    print("num: ",num%10)

def main():
    num:int=int(input("enter number: "))
    printOnes(num)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()