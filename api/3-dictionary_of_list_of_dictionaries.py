#!/usr/bin/python3
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    users = requests.get(f'{API_URL}/users').json()
    todos = requests.get(f"{API_URL}/todos").json()

    data = {}
    for task in todos:
        user_id = task['userId']
        if user_id not in data:
            data[user_id] = []
        data[user_id].append({
            "username": next(user['username']
                             for user in users
                             if user['id'] == user_id),
            "task": task['title'],
            "completed": task['completed']
        })
    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)
