def main():
    secretNum:int=44
    guess:int=int(input("guess my number btw 1 and 99: "))
    
    while(secretNum!=guess):
        if(secretNum>guess):
            print("your guess is too low!!")
        elif(secretNum<guess):
            print("your guess is to high!")
        guess=int(input("guess again!!: "))
        
    print("correct!!")
        
        
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()