# import firebase_admin
# from firebase_admin import credentials, firestore
# Important Note : Need Python 64 bit version for windows

# Importing Streamlit
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import os
from pathlib import Path

# Load in credentials to access firebase db
# abspath = os.path.abspath('serviceAccountKey.json')
# cred = credentials.Certificate(abspath)  # Never store in public
# firebase_admin.initialize_app(cred)

# firestore.Client.from_service_account_json("firestore-key.json")
# Navigating to correct document - firestore
# db = firestore.client()
path = Path(__file__).parent / "serviceAccountKey.json"
db = firestore.Client.from_service_account_json(path)

collection = db.collection('user')


# Reads Data From All Documents
def read_all_data():
    user_list = []
    docs = collection.get()
    for doc in docs:
        user_list.append(doc.to_dict())
    return user_list


# Return Certain Data Based on condition
def read_data():
    # Some Code
    return 1  # Temporary


# Sample Test
final_output = read_all_data()
print(final_output)

for output in final_output:
    str_out = f"The list of people is {output['lname']}"
    st.write(str_out)


# Test Class to Connect with Flask - Need to Change to Allow Parameters Later
class FirebaseData:

    def __init__(self, names):
        self.lNames = []
        self.fNames = []
        self.totalNames = []

    def get_lnames(self):  # Need to Change to Take in Parameters from other class Instead
        for outputs in final_output:
            self.lNames.append(outputs['lName'])
        return self.lNames

    def get_fnames(self):  # Need to Change to Take Parameters in from other class Instead
        for outputs in final_output:
            self.fNames.append(outputs['fname'])
        return self.fNames

    def get_completenames(self):
        for outputs in final_output:
            self.totalNames.append(outputs)
        return self.totalNames


print(FirebaseData.get_completenames(final_output))

