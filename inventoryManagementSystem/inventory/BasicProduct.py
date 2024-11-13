from db.db_handler import MongoDBHandler
from pymongo.errors import DuplicateKeyError, PyMongoError

class BasicProduct:
    def __init__(self) -> None:
        self.ProductID: int = 0000
        self.ProductName: str = "******"
        self.price: float = 0.0
        self.unitName: str = "***"
        self.stock: int = 0
        
        # Initialize MongoDBHandler and get the collection
        db_handler = MongoDBHandler()
        self.collection = db_handler.get_collection("BasicProduct")

    def addProduct(self) -> None:
        try:
            # Gather product details
            self.ProductID = int(input("Enter ProductID (integer ID): "))
            self.ProductName = str(input("Enter Product Name: "))
            self.price = float(input("Enter the price of Product: "))
            self.unitName = str(input("Enter the unit name (pc, kg, dozen, etc.): "))
            self.stock = int(input("Enter the number of pieces in stock: "))  # New stock input
            
            # Create a dictionary for the product, including stock
            product_data = {
                "ProductID": self.ProductID,
                "ProductName": self.ProductName,
                "price": self.price,
                "unitName": self.unitName,
                "stock": self.stock  # Adding stock to product data
            }

            
            self.collection.insert_one(product_data)
            print("Product added successfully!")
        
        except DuplicateKeyError:
            print("Error: ProductID already exists. Please enter a different ProductID.")
        except ValueError:
            print("Error: Invalid input. Please enter correct data types for ProductID, price, stock, etc.")
        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        input("Press Enter to continue...")


    def showProduct(self) -> None:
        try:
            product_id = int(input("Enter the ProductID to view: "))
            product = self.collection.find_one({"ProductID": product_id})
            if product:
                print(f"Product Details:\nProductID: {product['ProductID']}\nProductName: {product['ProductName']}\nPrice: {product['price']}\nUnit: {product['unitName']}")
            else:
                print(f"No product found with ProductID {product_id}.")

        except ValueError:
            print("Error: Invalid ProductID format.")
        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        input("Press Enter to continue...")


    def showAll(self) -> None:
        try:
            products = self.collection.find()
            
            # Check if there are any products by converting to a list and checking its length
            products_list = list(products)
            
            if len(products_list) > 0:
                for product in products_list:
                    print(f"ProductID: {product['ProductID']}, ProductName: {product['ProductName']}, Price: {product['price']}, Unit: {product['unitName']}")
            else:
                print("No products found in the database.")


        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        input("Press Enter to continue...")


    def editPrice(self) -> None:
        try:
            product_id = int(input("Enter the ProductID to edit price: "))
            new_price = float(input("Enter the new price: "))
            result = self.collection.update_one({"ProductID": product_id}, {"$set": {"price": new_price}})
            if result.modified_count > 0:
                print(f"Price of product with ProductID {product_id} updated to {new_price}.")
            else:
                print(f"No product found with ProductID {product_id}.")

        except ValueError:
            print("Error: Invalid input for ProductID or price.")
        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        input("Press Enter to continue...")


    def editName(self) -> None:
        try:
            product_id = int(input("Enter the ProductID to edit name: "))
            new_name = str(input("Enter the new name: "))
            result = self.collection.update_one({"ProductID": product_id}, {"$set": {"ProductName": new_name}})
            if result.modified_count > 0:
                print(f"Name of product with ProductID {product_id} updated to {new_name}.")
            else:
                print(f"No product found with ProductID {product_id}.")
        except ValueError:
            print("Error: Invalid input for ProductID or name.")
        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        input("Press Enter to continue...")


    def updateStock(self) -> None:
        try:
            product_id = int(input("Enter the ProductID to update stock: "))
            new_stock = int(input("Enter the new stock value: "))
            result = self.collection.update_one({"ProductID": product_id}, {"$set": {"stock": new_stock}})
            if result.modified_count > 0:
                print(f"Stock for product with ProductID {product_id} updated to {new_stock}.")
            else:
                print(f"No product found with ProductID {product_id}.")
        except ValueError:
            print("Error: Invalid input for ProductID or stock value.")
        except PyMongoError as e:
            print(f"MongoDB Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        input("Press Enter to continue...")

