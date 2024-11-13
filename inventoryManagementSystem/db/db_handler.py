# db/db_handler.py
from pymongo import MongoClient
from pymongo.database import Database

class MongoDBHandler:
    _instance = None

    # Type annotations for client and db
    client: MongoClient
    db: Database

    def __new__(cls, uri: str = 'mongodb://localhost:27017/', db_name: str = 'inventory_db'):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(uri)
            cls._instance.db = cls._instance.client[db_name]
            # Ensure the ProductID field is unique when creating the collection
            cls._instance.db["BasicProduct"].create_index([("ProductID", 1)], unique=True)
        return cls._instance
    
    def get_collection(self, collection_name: str):
        return self.db[collection_name]
