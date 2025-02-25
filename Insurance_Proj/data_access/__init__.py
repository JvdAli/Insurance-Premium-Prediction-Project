import pandas as pd
import json
import os, sys
from dotenv import load_dotenv
import pymongo

def mongodb_client():

    #creating filepath for the .env file 
    ROOT_DIR = os.getcwd()
    env_file_path = os.path.join(ROOT_DIR, '.env')

    #load the environment filepath(1st line) & variables from the .env file(3 line below)
    load_dotenv(dotenv_path = env_file_path)
    username = os.getenv("USER_NAME")
    password = os.getenv("PASS_WORD")
    cluster_name = os.getenv("CLUSTER_LABEL")

    #constructing the MongoDB connection URL using the variables
    mongo_db_url = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    print(mongo_db_url)

    #creating a MongoClient object 
    client = pymongo.MongoClient(mongo_db_url)

    #returning the client object
    return client