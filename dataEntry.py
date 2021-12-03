from pymongo import MongoClient
import pandas as pd


demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["De-dupe"]

myCollection = myDatabase["Data"]

df = pd.read_csv('Generated.csv')

# For Entering CSV rows into Mongo_DB
for index, row in df.iterrows():
    MRN = row['MRN Number']
    firstName=row['First Name']
    lastName = row['Last Name']
    DOB = row['DOB']
    phone = row['Phone Number']
    email = row['Email']
    state = row['State']
    pincode = row['Pincode']
    yoe= row['Years of Exp.']
    specialization = row['Specialization']
    education = row['Education']

    myCollection.insert_many([{
    "MRN": MRN,
    "First Name": firstName,
    "Last Name": lastName,
    "DOB": DOB, 
    "State": state,
    "Pincode": pincode,
    "Phone": phone, 
    "Years of experience": yoe,
    "Specialization":specialization,
    "Education":education
    }])

print("Complete")
