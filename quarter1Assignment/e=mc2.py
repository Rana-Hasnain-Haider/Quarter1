def main():
    mass:float=float(input("enter mass: "))
    c:int=299792458.0
    e:float = (mass*(c**2))
    print("the energy is: ",e)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()