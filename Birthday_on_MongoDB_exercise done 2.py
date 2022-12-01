#Importing pymongo module
import pymongo 


#Creating the Folder path for the collection
client = pymongo.MongoClient("mongodb+srv://alexanderakiode:Greats11@cluster0.qcurgqp.mongodb.net/?retryWrites=true&w=majority")
db = client['Birthdays']
col = db["birthday_collection"]

#Finding and inserting the content of the collection from MongoDB
#birthday = col.find_one()

#Finding and inserting the content of the collection from MongoDB
#Removing _id from the output
birthday = col.find_one({},{ "_id": 0,})

#Using the Lab 6 coding line:
#Printing the output pretext
print(">>> Welcome to the birthday dictionary. We know the birthdays of: ")

#To call the names in the birthday collection, 
#call the values out from the birthday variable and print
for name in birthday:
    print(name)
  
#Defining the input functions for the statement using variable name_on_request
#Calling both the key = name and the value = birthdate
name_on_request = input(">>> Who's birthday do you want to look up : ? ")
for name, birthdate in birthday.items():
    #Defining the condition for name print for subsequent birthdate print
    if name == name_on_request: 
        print(">>>%s's birthday is %s: " %(name, birthdate))

