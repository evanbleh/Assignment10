# Name: Assignment 10 Group 3
# email: le2dc@mail.uc.edu, blehet@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: November 9 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: retrieves information from a public APIs database, parsing the data into a dictionary. It then prints out the name and description of the first API entry
# Citations: n/a
# Anything else that's relevant: n/a

#main

import json
import requests

from APIClass.APIClass import *

if __name__ == "__main__":
    API = readJSON('https://api.publicapis.org/entries')
    api_data = API.get_api_data()
    

    # Print the name and description of the first API entry
    print("API Name: " + api_data[0]['API'])
    print("API Description: " + api_data[0]['Description'])