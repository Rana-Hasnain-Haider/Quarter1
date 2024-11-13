def main():
    farenheit:float
    celcius:float
    farenheit=float(input("enter temp in farenheit: "))
    celcius=(farenheit-32)*5.0/9.0
    print("the temp in celcius is: ",celcius)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()