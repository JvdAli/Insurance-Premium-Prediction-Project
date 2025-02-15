import pymongo 
import pandas as pd
import json , os , sys
import logging
from dotenv import load_dotenv

#mongodb connection url , taken from mongodb
uri = "mongodb+srv://jvdaliMDB:12345@cluster0.cqzzm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# creating a mongodb client object to connect to the server
client = pymongo.MongoClient(uri)


DATA_FILE_PATH = r"D:\DS-AB\Project\MLOps_Pro_Insurance\Insurance-Premium-Prediction-Project\insurance_data.csv"  # data file path in local machine , to dump in mongodb
DATABASE_NAME = "Insurance_Data"          # variable for mongodb database name 
COLLECTION_NAME = "Data_Collection"       # variable for mongodb collection name, records are known as collections in mongodb

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)              #reading data from local machine using panda library
    print(f"Rows and columns: {df.shape}")        #checking shape of the data by printing on terminal ,prior inseting into mongodb

    df.reset_index(drop = True, inplace = True)   #dropping index of the dataset permanently(True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])                         #checking 1st collection of the dataset by printing on terminal ,after transformation into collection is done

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)  

    #client[DATABASE_NAME][COLLECTION_NAME] accesses the specific database and collection in MongoDB.
    #inserting tranformed dataset into mongodb to insert multiple collections into MongoDB


    # list(json.loads(df.T.to_json()).values())
    # df.T: This transposes the DataFrame, swapping rows with columns.
    # df.T.to_json(): This converts the transposed DataFrame to a JSON string.
    # json.loads(...): This parses the JSON string into a Python dictionary.
    # .values(): This gets the values of the dictionary (which correspond to the columns in the original DataFrame after transposition).
    # list(...): This converts the dictionary view object into a list.