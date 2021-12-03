from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd
import json
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["De-dupe"]
myCollection = myDatabase["Data"]

def checkDuplicates(MRN,firstName,lastName,DOB,State,Pincode,
                    Phone,YOE,Specialization,Education,MRNscale,fNamescale,
                    lNamescale,DOBscale,Statescale,Pincodescale,Phonescale,
                    YOEscale,Specializationscale,Educationscale):
    # getting the details etc
    mrnWeight = float(MRNscale)
    fnameWeight = float(fNamescale)
    lnameWeight = float(lNamescale)
    dobWeight = float(DOBscale)
    phoneWeight = float(Phonescale)
    pincodeWeight = float(Pincodescale)
    stateWeight = float(Statescale)
    yoeWeight = float(YOEscale)
    spezWeight = float(Specializationscale)
    eduWeight = float(Educationscale)

    # USER INPUTS - SINGLE CUSTOMER SCENARIO
    mrn_inp = MRN
    fname_inp = firstName
    lname_inp = lastName
    dob_inp = DOB
    phone_inp = Phone
    # s_phone_inp = input("Enter secondary phone number: ")
    # email_inp = input("Enter email address: ")
    pincode_inp = Pincode
    state_inp = State
    yoe_inp = YOE
    spez_inp = Specialization
    edu_inp = Education

    flag = 0
    data = []
    for document in myCollection.find():
        score = 0

        mrnSimilarityScore = lev.ratio(document.get('MRN').lower(), mrn_inp.lower())
        if mrnSimilarityScore >= mrnWeight:
            score = score + 1

        fnameSimilarityScore = lev.ratio(document.get('First Name').lower(), fname_inp.lower())
        if fnameSimilarityScore >= fnameWeight:
            score = score + 1

        lnameSimilarityScore = lev.ratio(document.get('Last Name').lower(), lname_inp.lower())
        if lnameSimilarityScore >= lnameWeight:
            score = score + 1

        dobSimilarityScore = lev.ratio(document.get('DOB'),dob_inp)
        if dobSimilarityScore >= dobWeight:
            score = score + 1

        phoneSimilarityScore = lev.ratio(str(document.get('Phone')), phone_inp)
        if phoneSimilarityScore >= phoneWeight:
            score = score + 1
        
        pincodeSimilarityScore = lev.ratio(str(document.get('Pincode')),pincode_inp)
        if pincodeSimilarityScore >= pincodeWeight:
            score = score + 1

        stateSimilarityScore = lev.ratio(document.get('State'), state_inp)
        if stateSimilarityScore >= stateWeight:
            score = score + 1

        spezSimilarityScore = lev.ratio(document.get('Specialization'), spez_inp)
        if spezSimilarityScore >= spezWeight:
            score = score + 1

        eduSimilarityScore = lev.ratio(document.get('Education'), edu_inp)
        if spezSimilarityScore >= spezWeight:
            score = score + 1

        similarityScore = (mrnSimilarityScore*mrnWeight + fnameSimilarityScore*fnameWeight +
                        lnameSimilarityScore*lnameWeight + dobSimilarityScore*dobWeight +
                        phoneSimilarityScore*phoneWeight + pincodeWeight*pincodeWeight + 
                        stateSimilarityScore*stateWeight + spezSimilarityScore*spezWeight +
                        eduSimilarityScore*eduWeight) / (mrnWeight + fnameWeight + lnameWeight + dobWeight + phoneWeight +
                                                         pincodeWeight + stateWeight + spezWeight +
                                                            eduWeight)


        if score >= 8 or similarityScore > 0.6:
            data.append([document.get('MRN'), document.get('First Name'), document.get('Last Name'), document.get('DOB'),document.get('Phone'), document.get('Pincode'), document.get('State'), document.get('Years of experience'), document.get('Specialization'), document.get('Education'), similarityScore])
            flag = 1

    count = 1
    response = {'check': flag,
                'data': []}
    
    if flag == 0:
        print('---Data unique - PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    else:
        print('--- SIMILAR ENTRIES FOUND ---')
        data_similarity = pd.DataFrame(data, columns=['MRN', 'First Name', 'Last Name', 'DOB', 'Phone', 'Pincode', 'State', 'Years of experience', 'Specialization', 'Education', 'Similarity Score'])
                                       
        data_similarity = data_similarity.sort_values('Similarity Score', ascending=False)
        # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
        for index, row in data_similarity.iterrows():
            print(count)
            print("SIMILARITY SCORE: ", row['Similarity Score'])
            print("MRN : ", row["MRN"])
            print("Name: ", row['First Name']+' '+row['Last Name'])
            print("DOB: ", row['DOB'])
            print("Phone: ", row['Phone'])      
            print("Pincode: ", row["Pincode"])
            print("State: ", row["State"])
            print("Years of Exp.: ", row["Years of experience"])
            print("Specialization : ", row["Specialization"])
            print("Education: ", row["Education"])
            print("")
                        
            details={ 
                'MRN': row["MRN"],
                'First Name': row['First Name'],
                    'Last Name': row['Last Name'],
                    'DOB': row['DOB'],
                    'Phone Number': row['Phone'],
                    'Pincode': row["Pincode"],
                    'State': row["State"],
                    'Years of experience': row["Years of experience"],
                    'Specialization': row["Specialization"],
                    'Education': row["Education"],
                    'Similarity Score': row['Similarity Score']
            }
            response['data'].append(details)
            count = count + 1
            if count == 6:
                break
        data_similarity.to_csv("SimilarData_SingleRowInput.csv")

    return response

