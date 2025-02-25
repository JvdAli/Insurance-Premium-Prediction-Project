import os,sys
from Insurance_Proj.logger import logging 
from Insurance_Proj.exception import CustomException 
from datetime import datetime

FILE_NAME = "insurance.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
MODEL_FILE_NAME = "model.pkl"

TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise CustomException(e,sys)    


class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="Insurance_Data"
            self.collection_name="Data_Collection"

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")  #folder

            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)

            self.test_size = 0.2
        except Exception  as e:
            raise CustomException(e,sys)      

            
# Convert data into dictionary format
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise CustomException(e,sys)          

# class DataValidationConfig:
    
#     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
#         self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir , "data_validation")
#         self.report_file_path=os.path.join(self.data_validation_dir, "report.yaml")
#         self.missing_threshold:float = 0.2
#         self.base_file_path = os.path.join("insurance.csv")


