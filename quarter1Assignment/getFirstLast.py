
def get_first_element(lst):
        print(lst[0])

def get_last_element(lst:list):
    size:int=len(lst)
    print(lst[size-1])
    

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)
    get_last_element(lst)


if __name__ == '__main__':
    main()

