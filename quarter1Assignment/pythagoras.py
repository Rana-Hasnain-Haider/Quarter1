import math
def main():
    AB:float=float(input("enter length of side AB: "))

    BC:float=float(input("enter length of side BC: " ))
    AC:float=math.sqrt((AB**2)+(BC**2))
    print("the hypotenuse is: ",AC)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()