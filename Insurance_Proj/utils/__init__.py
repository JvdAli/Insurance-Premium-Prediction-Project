
import os, sys
from Insurance_Proj.exception import CustomException
from Insurance_Proj.logger import logging
from datetime import datetime
from Insurance_Proj.constant import *
import yaml
import pandas as pd
from Insurance_Proj.data_access import mongodb_client
import numpy as np
import dill

# creating function to fetch data from mongodb database and connvert json into dataframe.
def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    try:
        
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")

        client=mongodb_client()   #creating object of the function created in data_access module
        df = pd.DataFrame(list(client[database_name][collection_name].find()))

        logging.info(f"Found columns: {df.columns}")

        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise CustomException(e, sys)