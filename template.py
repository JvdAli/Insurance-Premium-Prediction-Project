import os, sys
from pathlib import Path
import logging

#asking project name 
while True:
    project_name = input("Enter the project name: ")
    if project_name!= "":                                 #if project name not entered then keep asking
        break                                             #if project name is entered, break the loop and proceed


#list of all necessary folders & files
List_of_files = [
    #folders & files inside project folder
     ".github/workflows/.gitkeep",                        # to protect credentials/files from being uploaded to github
    f"{project_name}/__init__.py",                        # for converting project folder into a package
    f"{project_name}/components/__init__.py"
    f"{project_name}/entity/__init__.py",   
    f"{project_name}/config.py",
    
    f"{project_name}/constant/__init__.py",
    f"{project_name}/utils/__init__.py",

    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",

    f"{project_name}/predictor/__init__.py",
    f"{project_name}/pipeline/__init__.py",

    #folders & files outside project folder
    f"configs/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py"
]

#List of all necessary folders & files to be created
for filepath in List_of_files: 
    filepath = Path(filepath)        #It provides cross-platform compatibility, automatically handling path separators (like / on Unix and \ on Windows).
    filedir,filename = os.path.split(filepath)  #It returns a tuple with these two components: (filedir, filename)


    #below if statement to create folders
    if filedir != "":
        #os.mkdir()  : only creates the last folder in the path. Intermediate folders must already exist.
        #os.makedirs() : To create an entire folder structure(folders & file)
        os.makedirs(filedir, exist_ok=True)                 #create folder if that folder doesnt exist(True)

    #below if statement to create files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):    # if file size is zero overwrite else skip
        with open (filepath, "w") as f:
            pass                            # w is used to open the file in write mode and pass/leave it
            logging.info(f"Creating empty file:{filepath}")
    else:
            logging.info(f"{filename} already exists)")