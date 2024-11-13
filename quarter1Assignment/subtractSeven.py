def main():
	num: int = int(input("enter number: "))
	num = subtract_seven(num)
	print("this should be: ", num)

def subtract_seven(num):
	num = num - 7
	return num


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()