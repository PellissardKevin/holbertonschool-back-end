#!/usr/bin/python3
"""Gather data from API"""

from sys import argv
import requests


if __name__ == '__main__':
    # todo info
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
    todos_data = todos.json()
    # user info
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    users_data = users.json()

    completed_tasks = [task for task in todos_data if task['completed']]

    user_name = users_data["name"]
    len_completed_tasks = len(completed_tasks)
    total_todo = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
            user_name,
            len_completed_tasks,
            total_todo))

    for task in completed_tasks:
        print(f"\t {task['title']}")
