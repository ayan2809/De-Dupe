from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd

# from fuzzywuzzy import fuzz as lev

demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["De-dupe"]
myCollection = myDatabase["Data"]

def checkDuplicates(MRN,firstName,lastName,DOB,State,Pincode,Phone,YOE,Specialization,Education,MRNscale,fNamescale,lNamescale,DOBscale,Statescale,Pincodescale,Phonescale,YOEscale,Specializationscale,Educationscale):
    # getting the details etc
    print(MRN)
    print(firstName)
    print(lastName)
    print(DOB)
    print(State)
    print(Pincode)
    print(Phone)
    print(YOE)
    print(Specialization)
    print(Education)
    print(MRNscale)
    print(fNamescale)
    print(lNamescale)
    print(DOBscale)
    print(Statescale)
    print(Pincodescale)
    print(Phonescale)
    print(YOEscale)
    print(Specializationscale)
    print(Educationscale)

# DECLARE THRESHOLDS -  SLIDER CONCEPT IN UI
#filename2 = input("Enter the weight file path.")
# datafile=pd.read_csv('weight_input.csv',encoding= 'unicode_escape')
# # print(datafile)
# for index, row in datafile.iterrows():
#     mrnWeight = row['mrnWeight']
#     fnameWeight = row['fnameWeight']
#     lnameWeight = row['lnameWeight']
#     dobWeight = row['dobWeight']
#     phoneWeight = row['phoneWeight']
#     emailWeight = row['emailWeight']
#     pincodeWeight = row['pincodeWeight']
#     stateWeight = row['stateWeight']
#     # yoeWeight = 0.5
#     spezWeight = row['spezWeight']
#     eduWeight = row['eduWeight']

# print(mrnWeight)
# print(fnameWeight)
# print(lnameWeight)
# print(dobWeight)
# print(phoneWeight)
# print(emailWeight)
# print(pincodeWeight)
# print(stateWeight)
# print(spezWeight)
# print(eduWeight)
# flag = 0
# data = []

# # USER INPUTS - BULK DATA
# filename = input("Enter the file path.")
# df = pd.read_csv(filename)
# for index, row in df.iterrows():
#     mrn_inp = row['MRN Number']
#     fname_inp = row['First Name']
#     lname_inp = row['Last Name']
#     dob_inp = row['DOB']
#     phone_inp = str(row['Phone Number'])
#     email_inp = row['Email']
#     pincode_inp = str(row['Pincode'])
#     state_inp = row['State']
#     yoe_inp = str(row['Years of Exp'])
#     spez_inp = row['Specialization']
#     edu_inp = row['Education']

#     maxSS = 0
#     finalID=""
#     for document in myCollection.find():
#         score = 0
#         mrnSimilarityScore = lev.ratio(document.get('MRN').lower(), mrn_inp.lower())
#         if mrnSimilarityScore >= mrnWeight:
#             score = score + 1

#         fnameSimilarityScore = lev.ratio(document.get('First Name').lower(), fname_inp.lower())
#         if fnameSimilarityScore >= fnameWeight:
#             score = score + 1

#         lnameSimilarityScore = lev.ratio(document.get('Last Name').lower(), lname_inp.lower())
#         if lnameSimilarityScore >= lnameWeight:
#             score = score + 1

#         dobSimilarityScore = lev.ratio(document.get('DOB'), dob_inp)
#         if dobSimilarityScore >= dobWeight:
#             score = score + 1

#         phoneSimilarityScore = lev.ratio(str(document.get('Phone Number')), phone_inp)
#         if phoneSimilarityScore >= phoneWeight:
#             score = score + 1

#         emailSimilarityScore = lev.ratio(document.get('Email'), email_inp)
#         if emailSimilarityScore >= emailWeight:
#             score = score + 1

#         pincodeSimilarityScore = lev.ratio(str(document.get('Pincode')), pincode_inp)
#         if pincodeSimilarityScore >= pincodeWeight:
#             score = score + 1

#         stateSimilarityScore = lev.ratio(document.get('State'), state_inp)
#         if stateSimilarityScore >= stateWeight:
#             score = score + 1

#         spezSimilarityScore = lev.ratio(document.get('Specialization'), spez_inp)
#         if spezSimilarityScore >= spezWeight:
#             score = score + 1

#         eduSimilarityScore = lev.ratio(document.get('Education'), edu_inp)
#         if spezSimilarityScore >= spezWeight:
#             score = score + 1

#         tsimilarityScore = (mrnSimilarityScore * mrnWeight + fnameSimilarityScore * fnameWeight +
#                            lnameSimilarityScore * lnameWeight + dobSimilarityScore * dobWeight +
#                            phoneSimilarityScore * phoneWeight + emailSimilarityScore * emailWeight +
#                            pincodeSimilarityScore * pincodeWeight + stateSimilarityScore * stateWeight + spezSimilarityScore * spezWeight +
#                            eduSimilarityScore * eduWeight) / (
#                                       mrnWeight + fnameWeight + lnameWeight + dobWeight + phoneWeight
#                                       + emailWeight + pincodeWeight + stateWeight + spezWeight +
#                                       eduWeight)
#         if tsimilarityScore>maxSS:
#             maxSS = tsimilarityScore
#             finalID=document.get('_id')
#             # cursor = collection.find({})
#             # for document in cursor:
#             #     print document['_id']
#     # for document in myCollection.find():
#     #     print(document.find({"_id": finalID}))
#     itm = myDatabase.myCollection.find_one({"_id":finalID})
#     print(itm)
#     #print( itm.get('_id'))
#     #print(db.collection.find({"_id": ObjectId(finalID)}))
#     if maxSS> 0.90:
#         DUP = 'D'
#         data.append(
#             [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
#              edu_inp, maxSS, DUP])
#         maxSS = 0

#     elif maxSS > 0.65:
#         DUP = 'P'
#         data.append(
#             [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
#              edu_inp, maxSS, DUP])
#         maxSS = 0

#     else:
#         DUP = 'U'
#         data.append(
#             [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
#              edu_inp, maxSS, DUP])
#         maxSS = 0


# data_summary = pd.DataFrame(data, columns=['MRN', 'First Name', 'Last Name', 'DOB', 'Phone Number', 'Email',
#                                                   'Pincode', 'State', 'Years of Exp', 'Specialization', 'Education',
#                                                   'SimilarityScore', 'DUP'])
# data_summary.to_csv("Output.csv")

# print("Output file generated. Check directory.")

# # REPORT GENERATION - WRITING IT TO A FILE.
# size = len(data_summary.index)
# unique_count = (data_summary['DUP'].values == 'U').sum()
# partial_count = (data_summary['DUP'].values == 'P').sum()
# duplicate_count = (data_summary['DUP'].values == 'D').sum()
# unique_count_perc = round(unique_count/size * 100, 2)
# partial_count_perc = round(partial_count/size * 100, 2)
# duplicate_count_perc = round(duplicate_count/size * 100, 2)
# strlist = []
# line1 = "--------Summary of Input Data----------\n"
# line2 = "\n"
# line3 = f"Total numbers of rows in the input data set: {size}."
# line4 = f"\nUnique Entry Count: {unique_count} ({unique_count_perc} %)\n"
# line5 = f"Duplicate Entry Count: {duplicate_count} ({duplicate_count_perc} %)\n"
# line6 = f"Partial Similarity Entry Count: {partial_count} ({partial_count_perc} %)\n"
# strlist = [line1, line2, line3, line4, line5, line6]

# f= open("Report10k.txt", "w+")
# for line in strlist:
#     f.write(str(line))
# print("Report Generated! Check file in directory")