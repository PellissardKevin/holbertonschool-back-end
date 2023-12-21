#!/usr/bin/python3
"""Script to use a REST API, returns information about
all tasks from all employees and export in JSON"""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{API_URL}/users").json()
    tasks = requests.get(f"{API_URL}/todos").json()

    dict_users_tasks = {
        user.get('id'):
        [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in tasks if task.get('userId') == user.get('id')
        ] for user in users
    }

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_users_tasks, file)
