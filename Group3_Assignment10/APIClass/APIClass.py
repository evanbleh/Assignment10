# Name: Assignment 10 Group 3
# email: le2dc@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: November 9 2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: retrieves information from a public APIs database, parsing the data into a dictionary. It then prints out the name and description of the first API entry
# Citations: n/a
# Anything else that's relevant: n/a

#class

import json
import requests

class readJSON:
    def __init__(self, url):
        self.type = type
        self.url = url
    def get_api_data(self):
        response = requests.get(self.url)
        json_string = response.content
        parsed_json = json.loads(json_string)

        return parsed_json['entries'] #Return the list of API entries