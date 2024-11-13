from db.db_handler import MongoDBHandler

class SaleReport:
    def __init__(self):
        db_handler = MongoDBHandler()
        self.SaleCollection = db_handler.get_collection("soldProduct")

    def generate_report(self):
        # Fetch all records from the collection
        sold_data = self.SaleCollection.find()
        
        # Display in a structured format
        print("Sales Report:")
        print(f"{'ProductID':<12} {'ProductName':<20} {'Price':<10} {'Unit':<10} {'Pieces Sold':<12} {'total bill':<12}")
        print("-" * 65)
        
        # Loop through the sold data and print each entry
        for data in sold_data:
            print(f"{data['ProductID']:<12} {data['ProductName']:<20} {data['price']:<10} {data['unitName']:<10} {data['piecesSold']:<12} {data['totalPrice']:<12}")
