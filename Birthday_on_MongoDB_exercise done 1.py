#Importing pymongo
import pymongo

#Importing json
import json

#Importing MongoClient 
from pymongo import MongoClient

#Creating client variable on MongoDB
client = MongoClient("mongodb+srv://alexanderakiode:Greats11@cluster0.qcurgqp.mongodb.net/?retryWrites=true&w=majority")

#Creating the database called Birthdays on MongoDB
db = client['Birthdays']

#Creating the collection called birthday_collection on MongoDB
collection = db.birthday_collection

#Loading the json file and assigning the content of the file 
#into the variable birthday unto MongoDB
birthday = json.load(open("My_Birthdays_3.json"))

#Calling the function insert to insert the file unto MongoDB
collection.insert_one(birthday)
