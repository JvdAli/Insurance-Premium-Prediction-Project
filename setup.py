#The setup.py file is critical for packaging, installing, and managing dependencies in an MLOps project. 
# It helps ensure that your machine learning code is easily installable, reproducible, and shareable, 
# while also ensuring that all required libraries and versions are in place for your machine learning workflows.

from setuptools import find_packages, setup
from typing import List

REQUIRMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# HYPHEN_E(-e) stands for editable mode : 
# In editable mode, pip(package manager) will install the package in a way that it's possible to edit the code and test it without reinstalling the package.
# DOT(.) refers to the current directory

def get_requirements(REQUIRMENTS_FILE_NAME:str)->List[str]:

    with open(REQUIRMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()       #reading requirement file line by line
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list] # removing \n after each line

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)  #to ensure setup file is not triggered again from requirements.txt
        return requirement_list

# def get_requirements(file_path:str)->List[str]:       #this function will return the list of requirements
#     requirements=[]

#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace('\n',"") for req in requirements]

#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)   ##to ensure setup file is not triggered again from requirements.txt

#     return requirements


setup(
        name = "Insurance-Premium-Prediction-Project",
        version = "0.0.1",
        description = "Insurance-Premium-Prediction-Project",
        author = "Javed Ali",
        author_email = "jvdali.e@gmail.com",
        packages = find_packages(),                                 #find packages within this project
        install_requires =get_requirements('requirements.txt')      #passing requirement.txt to the created function
    )