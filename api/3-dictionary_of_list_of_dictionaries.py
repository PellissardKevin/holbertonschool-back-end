#!/usr/bin/python3
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
import requests
from sys import argv

API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":

    users = requests.get(f"{API_URL}/users").json()
    todos = requests.get(f"{API_URL}/todos").json()

    dict_users_tasks = {}

    for task in todos:

        user_id = task['userId']

        if user_id not in dict_users_tasks:
            dict_users_tasks[user_id] = []

        dict_users_tasks[user_id].append({
            "username": next(user['username']
                             for user in users
                             if user['id'] == user_id),
            "task": task['title'],
            "completed": task['completed']
        })

    with open(f"{argv[1]}.json", "w") as file:
        json.dump(dict_users_tasks, file)
