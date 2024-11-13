def inRange(low:int,high:int,num:int):
    if(num<=low and num<=high):
        return True
    else:
        False
def main():
    num:int=int(input("enter number: "))
    
    print(inRange(33,66,num))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()