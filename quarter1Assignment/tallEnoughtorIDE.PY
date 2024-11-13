def main():
    maxHeight:int = 20
    num:int=int(input("enter height: "))
    if(num>=maxHeight):
        print("tall enough to ride!!")
    else:
        print("not tall enough")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()