def sum(arr:list)->int:
    res:int=0
    for a in arr:
        res=res+a
    return res
        
def main():
    ch:str
    arr:list[int]=[]
    while(1):
        ch=input("enter number (press space to exit: )")
        if(ch==" "):
            break
        
        arr.append(int(ch))
    
    
    print(sum(arr))
        
        
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()