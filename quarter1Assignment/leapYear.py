def main():
    year:int=int(input("enter the year: "))
    if(year%4==0 and (year%100!=0 or year%400==0)):
        print(f"{year} is a leap year")
    else:
        print("the {year} year is not a leap year")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()