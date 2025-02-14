import logging
import os, sys
from datetime import datetime

LOG_DIR_Name = "logs"        #log folder for storing log files
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR_Name)    #log folder path
os.makedirs(LOG_DIR_PATH, exist_ok=True)     #creating log folder


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"  
Log_file_name = f"log_{CURRENT_TIME_STAMP}.log"               # name format of the log file 


log_file_path = os.path.join(LOG_DIR_PATH,Log_file_name)   #joining log folder and log file

logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format ='%(asctime)s %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG )


