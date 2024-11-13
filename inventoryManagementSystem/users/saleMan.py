from inventory import BasicProduct, SoldProduct

class saleMan:
    def __init__(self):
        pass


    def SaleManMenu(self):
        productHandeler=BasicProduct()
        saleHandeler=SoldProduct()
        while True:
            print("-----------------------------------")
            print("INVENTORY MANAGEMENT SYSTEM")
            print("         Saleman MENU    ")
            print("-----------------------------------")
            print("1. Show Product")
            print("2. Show All Products")
            print("3. sell product")
            print("4. Exit")
            print("-----------------------------------")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                productHandeler.showProduct()
            elif choice == "2":
                productHandeler.showAll()
            elif choice=="3":
                saleHandeler.sellProduct()
                saleHandeler.generateBill()
            elif choice == "4":
                print("Exiting saleman Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
