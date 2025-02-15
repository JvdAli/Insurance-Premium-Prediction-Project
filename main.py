from Insurance_Proj.logger import logging 
from Insurance_Proj.exception import CustomException 
import os,sys
from Insurance_Proj.utils import get_collection_as_dataframe

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
        #   test_logger_and_expection()
        get_collection_as_dataframe(database_name="Insurance_Data", collection_name="Data_Collection")
    except Exception as e:
        print(e)

