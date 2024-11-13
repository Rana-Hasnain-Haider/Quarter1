def main():
    arr=[]
    ch=input("enter number or press enter to exit: ")
    while(ch!=""):
        arr.append(int(ch))
        ch=input("enter number or press enter to exit: ")
    
    print(arr)

    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()