def main():
    divisor:int=int(input("enter the divisor: "))
    dividend:int=int(input("enter the dividend: "))
    
    print("the quotent is: ",dividend/divisor)
    print("the remainder is: ",dividend%divisor)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()