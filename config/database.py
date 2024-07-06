from pymongo import MongoClient

client = MongoClient("mongodb+srv://diluth:drowssap@items.hwufrcw.mongodb.net/?appName=Items")

db = client.todo_db

collection_name = db["todo_collection"]