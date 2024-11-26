from pymongo import MongoClient

def read_records():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["my_database"]
    collection = db["stock_price_data"]

    try:
        print("Fetching records from MongoDB...\n")
        for record in collection.find():
            print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    read_records()