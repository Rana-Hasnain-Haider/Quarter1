

def main():
    amt:int
    total:int=0
    choice:str
    fruits=dict({})
    choice=input("enter name of fruit(enter exit to exit: )")
    while(choice!="exit"):
        amt=int(input("enter the price of fruit"))
        fruits[choice]=amt
        choice=input("enter name of fruit(enter exit to exit: )")
    
    
    for fr,pr in fruits.items():
        print(f"how many {fr}: ")
        amt:int=int(input(" "))
        total=total+(amt*pr)
        
    print("total bill is: ",total)
        


    


# Python boilerplate.
if __name__ == '__main__':
    main()