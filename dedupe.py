from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd

# from fuzzywuzzy import fuzz as lev

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
    # s_phoneWeight = 0.7
    # emailWeight = 0.65
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

        phoneSimilarityScore = lev.ratio(str(document.get('Primary Phone Number')), phone_inp)
        if phoneSimilarityScore >= phoneWeight:
            score = score + 1
        
        # s_phoneSimilarityScore = lev.ratio(str(document.get('Secondary Phone Number')), s_phone_inp)
        # if s_phoneSimilarityScore >= s_phoneWeight:
        #     score = score + 1

        # emailSimilarityScore = lev.ratio(document.get('Email'), email_inp)
        # if emailSimilarityScore >= emailWeight:
        #     score = score + 1

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


        if score >= 8 or similarityScore > 0.75:
            data.append([document.get('MRN'), document.get('First Name'), document.get('Last Name'), document.get('DOB'),
                        document.get('Phone Number'), document.get('Pincode'), document.get('State'),
                        document.get('Years of experience'), document.get('Specialization'), document.get('Education'),
                        similarityScore])
            flag = 1

    count = 1
    if flag == 0:
        print('---Data unique - PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    else:
        print('--- SIMILAR ENTRIES FOUND ---')
        data_similarity = pd.DataFrame(data, columns=['MRN', 'First Name', 'Last Name', 'DOB', 'Primary Phone Number', 'Secondary Phone Number', 'Email',
                                                    'Pincode', 'State', 'Years of Exp.', 'Specialization', 'Education',
                                                    'SimilarityScore'])

        data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
        # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
        for index, row in data_similarity.iterrows():
            print(count)
            print("SIMILARITY SCORE: ", row['SimilarityScore'])
            print("MRN : ", row["MRN"])
            print("Name: ", row['First Name']+' '+row['Last Name'])
            print("DOB: ", row['DOB'])
            print("Primary Phone: ", row['Primary Phone Number'])
            print("Secondary Phone: ", row['Secondary Phone Number'])
            print("Email ID: ", row['Email'])
            print("Pincode: ", row["Pincode"])
            print("State: ", row["State"])
            print("Years of Exp.: ", row["Years of Exp."])
            print("Specialization : ", row["Specialization"])
            print("Education: ", row["Education"])
            print("")
            count = count + 1
            if count == 6:
                break
        data_similarity.to_csv("SimilarData_SingleRowInput.csv")


