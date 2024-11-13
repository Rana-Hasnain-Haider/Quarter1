from db.db_handler import MongoDBHandler
from typing import Any
class SoldProduct:
    def __init__(self) -> None:
        self.ProductID: int = 0000
        self.ProductName: str = "******"
        self.price: float = 0.0
        self.unitName: str = "***"
        self.pieceToSell: int = 0
        self.sold_items:list[Any] = [] 
        
        db_handler = MongoDBHandler()
        self.StockCollection = db_handler.get_collection("BasicProduct")
        self.SaleCollection = db_handler.get_collection("soldProduct")
        
    def sellProduct(self) -> None:
        try:
            while True:
                # Get product details from the user
                self.ProductID = int(input("Enter ProductID (or 0 to finish): "))
                if self.ProductID == 0:
                    break  # Exit loop when user enters 0 to finish
                
                self.pieceToSell = int(input("Enter quantity to sell: "))
                
                # Check if the product exists in the BasicProduct collection
                product = self.StockCollection.find_one({"ProductID": self.ProductID})
                
                if not product:
                    print(f"No product found with ProductID {self.ProductID}.")
                    continue
                
                # Check if the available stock is sufficient
                if self.pieceToSell > product['stock']:
                    print(f"Not enough stock available. Only {product['stock']} pieces are in stock.")
                    continue
                
                # Update the stock in BasicProduct collection
                new_stock = product['stock'] - self.pieceToSell
                self.StockCollection.update_one({"ProductID": self.ProductID}, {"$set": {"stock": new_stock}})
                print(f"Stock updated. {new_stock} pieces remaining.")
                
                # Create a dictionary for the sold product
                self.ProductName = product['ProductName']
                self.price = product['price']
                self.unitName = product['unitName']
                
                sold_data = {
                    "ProductID": self.ProductID,
                    "ProductName": self.ProductName,
                    "price": self.price,
                    "unitName": self.unitName,
                    "piecesSold": self.pieceToSell
                }
                
                # Add the sold product details to the soldProduct collection
                self.SaleCollection.insert_one(sold_data)
                print(f"Product with ProductID {self.ProductID} sold successfully!")
                
                # Add the item to the sold_items list for bill generation
                self.sold_items.append({
                    "ProductName": self.ProductName,
                    "piecesSold": self.pieceToSell,
                    "price": self.price,
                    "totalPrice": self.price * self.pieceToSell
                })
                
        
        except ValueError:
            print("Error: Invalid input. Please enter correct data types for ProductID or quantity.")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def generateBill(self) -> None:
        if not self.sold_items:
            print("No items sold. Bill cannot be generated.")
            return
        
        total_amount = 0
        print("\n----- Bill -----")
        for item in self.sold_items:
            print(f"{item['ProductName']}: {item['piecesSold']} x {item['price']} = {item['totalPrice']}")
            total_amount += item['totalPrice']
        
        print(f"\nTotal Amount: {total_amount}")
        input("Press Enter to continue...")

