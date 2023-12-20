#!/usr/bin/python3
"""Gather data to json"""

from sys import argv
import requests
import json


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    USER_ID = argv[1]

    user = requests.get(f'{API_URL}/users/{USER_ID}').json()
    todo_list = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            }
            for task in todo_list
        ]
    }
    with open(f"{USER_ID}.json", 'w') as json_file:
        json.dump(data, json_file)
