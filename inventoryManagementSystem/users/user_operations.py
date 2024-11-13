import bcrypt
from db.db_handler import MongoDBHandler

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(stored_hash: bytes, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

def save_user(db_handler: MongoDBHandler, username: str, password: str, collection:str):
    users_collection = db_handler.get_collection(collection)
    hashed_password = hash_password(password)
    user = {'username': username, 'password': hashed_password}
    users_collection.insert_one(user)
    print(f"User {username} saved successfully.")

# Function to verify user credentials
def verify_user(db_handler: MongoDBHandler, username: str, password: str,collection:str)->bool:
    users_collection = db_handler.get_collection(collection)
    stored_user = users_collection.find_one({'username': username})
    if stored_user and check_password(stored_user['password'], password):
        print("Password is correct!")
        return True
    else:
        print("Incorrect password.")
        return False
        
