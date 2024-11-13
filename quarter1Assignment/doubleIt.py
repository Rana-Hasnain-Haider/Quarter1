def main():
    num:int=int(input("enter number: "))
    double:int=num*2
    while(double<100):
        print(double)
        double=double*2


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()