#!/usr/bin/python3
"""Gather data to json"""

from sys import argv
import requests
import json

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user = requests.get(f'{API_URL}/users/{argv[1]}').json()
    todo_list = requests.get(f"{API_URL}/todos?userId={argv[1]}").json()

    data = {
        argv[1]: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            }
            for task in todo_list
        ]
    }

    with open(f'{argv[1]}.json', 'w') as file:
        json.dump(u_tasks, file)
