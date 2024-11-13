from inventory import BasicProduct, SoldProduct,SaleReport
class Manager:
    def __init__(self):
        pass

    def managerMenu(self):
        productHandeler=BasicProduct()
        saleHandeler=SoldProduct() 
        reportHandeler=SaleReport()
        while True:
            print("-----------------------------------")
            print("INVENTORY MANAGEMENT SYSTEM")
            print("         Manager MENU    ")
            print("-----------------------------------")
            print("1. Add Product")
            print("2. Show Product")
            print("3. Show All Products")
            print("4. Change Name of Product")
            print("5. Update Product Stock")
            print("6. Update Price")
            print("7. sell product")
            print("8. show report")
            print("9. Exit")
            print("-----------------------------------")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                productHandeler.addProduct()
            elif choice == "2":
                productHandeler.showProduct()
            elif choice == "3":
                productHandeler.showAll()
            elif choice == "4":
                productHandeler.editName()
            elif choice == "5":
                productHandeler.updateStock()
            elif choice == "6":
                productHandeler.editPrice()
            elif choice=="7":
                saleHandeler.sellProduct()
                saleHandeler.generateBill()
            elif choice=="8":
                reportHandeler.generate_report()
            elif choice == "9":
                print("Exiting Manager Menu.")
                break
            else:
                print("Invalid choice. Please try again.")

