def print_Multiple(line:str,itr:int):
    for i in range(itr):
        print(line)
def main():
    line:str=input("enter the line to print: ")
    num:int=int(input("enter times to print: "))
    print_Multiple(line,num)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()