def main():
    ch = input("Enter number (press Enter to exit): ")
    arr = []
    
    while ch != "":
        arr.append(int(ch))
        ch = input("Enter number (press Enter to exit): ")
    
    numRepeat = {}
    for a in arr:
        if a not in numRepeat:
            numRepeat[a] = 1  
        else:
            numRepeat[a] += 1 
    
    # Print results
    for num, itr in numRepeat.items():
        print(f"{num} is repeated {itr} times")

if __name__ == '__main__':
    main()
