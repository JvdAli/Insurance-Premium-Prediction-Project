from Insurance_Proj.logger import logging 
from Insurance_Proj.exception import CustomException 
import os,sys
from Insurance_Proj.utils import get_collection_as_dataframe
from Insurance_Proj.entity import config_entity   
from Insurance_Proj.entity.config_entity import DataIngestionConfig 
from Insurance_Proj.components.data_ingestion import DataIngestion

# def test_logger_and_expection():
#     try:
#     #    logging.info("Starting the test_logger_and_exception")
#     #    result = 3/0
#     #    print(result)
#     #    logging.info("Stoping the test_logger_and_exception")
#     except Exception as e:
#     #    logging.debug(str(e))
#        raise CustomException(e, sys)

if __name__=="__main__":
    try:
        # test_logger_and_expection()
        get_collection_as_dataframe(database_name="Insurance_Data", collection_name="Data_Collection")
        
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        #print(data_ingestion_config.to_dict())

        #data ingestion
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        print(e)

