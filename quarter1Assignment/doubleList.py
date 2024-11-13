def main():
    arr:list[int]=[1,2,3,4]
    arr2:list[int]=[]
    for a in arr:
        arr2.append(a*2)
    
    print(arr2)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()