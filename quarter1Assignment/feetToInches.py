def main():
    feet:float=float(input("enter foot to convert: "))
    inches:float=feet*12
    print(f"the inches in {feet} foot are: ",inches)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()