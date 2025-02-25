import os, sys
import pandas as pd , pandas as np
from Insurance_Proj.entity import config_entity 
from Insurance_Proj.entity import artifact_entity
from Insurance_Proj.logger import logging 
from Insurance_Proj.exception import CustomException 
from Insurance_Proj import utils
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):  #"data_ingestion_config" hinted to get type "config_entity.DataIngestionConfig" as paramter
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Exporting collection data as pandas dataframe")
            df:pd.DataFrame  = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name, 
                collection_name=self.data_ingestion_config.collection_name)

            #replace na with NAN
            df.replace(to_replace="na",value=np.NA,inplace=True)

            logging.info("Create feature store folder if not available")
            #extract the directory portion of a file path,making it useful when you need to work with file locations and need the directory without the filename
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path) 
            #create feature store folder if not available
            os.makedirs(feature_store_dir,exist_ok=True)
            logging.info("Save raw/original dataset in feature store folder")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            logging.info("split dataset into train and test set")
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size, random_state = 1)
            
            logging.info("create dataset folder if not available")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            logging.info("Save splitted data in dataset folder")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)
            
            #Prepare artifact
            # object of DataIngestionArtifact is being created and paths are assigned
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path, 
                test_file_path=self.data_ingestion_config.test_file_path)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e,sys) 



        

                 
