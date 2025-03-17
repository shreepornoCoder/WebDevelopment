import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    mydb = client["myDB"] # Creating Database
    mycollection = mydb["sample"] # creating collection

    data = [
        {"name":"Shreeporno", "marks":"95", "status":"Active"},
        {"name":"Raihan", "marks":"90", "status":"Active"}
    ]

    mycollection.insert_many(data)
