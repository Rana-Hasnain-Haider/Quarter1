def fibonacci(n)->int:
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
def main()->int:
    maxValue:int=int(input("enter the max value to print fib: "))
    
    for i in range(maxValue):
        print(fibonacci(i))  
    
         
    return 0
    



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()