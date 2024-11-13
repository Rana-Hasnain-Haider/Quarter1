from users.user_operations import save_user, verify_user
from db.db_handler import MongoDBHandler
from users.manager import Manager
from users.saleMan import saleMan

import getpass

# Initialize the database handler
db_handler = MongoDBHandler()
manager=Manager()
saleman=saleMan()
choice: str

while(True):
    print("-----------------------------------")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("         MAIN MENU    ")
    print("-----------------------------------")
    print("1. Create Manager")
    print("2. login as Manager")
    print("3. Create SalesMan")
    print("4. login as Salesman")
    print("5. exit")
    print("-----------------------------------")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Create username: ")
        password = getpass.getpass("Create your password: ")
        save_user(db_handler, username, password, "managers")
    elif choice == "2":
        username = input("Enter username to login: ")
        password = getpass.getpass("Enter password to login: ")
        if(verify_user(db_handler, username, password, "managers")):
            manager.managerMenu()
    elif choice == "3":
        username = input("Create username: ")
        password = getpass.getpass("Create your password: ")
        save_user(db_handler, username, password, "salesmans")
    elif choice == "4":
        username = input("Enter username to login: ")
        password = getpass.getpass("Enter password to login: ")
        if(verify_user(db_handler, username, password, "salesmans")):
            saleman.SaleManMenu()
    elif choice=="5":
        break
    else:
        print("bad choice!")
