import random

def main():
    die1:int
    die2:int
    die1 = random.randint(1,6)
    die2=random.randint(1,6)
    
    print("the die1: "+str(die1)+" the die2: "+str(die2))
    print("total is: ",die2+die1)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()