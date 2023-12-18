#!/usr/bin/python3
"""Gather data to json"""

from sys import argv
import requests
import json


if __name__ == '__main__':
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos',
        params={"_expand": "user"})
    data = response.json()

    u_tasks = {argv[1]: []}
    for task in data:
        task_dict = {
            "task": task['title'],
            "completed": task['completed'],
            "username": task['user']['username']
        }
        u_tasks[argv[1]].append(task_dict)

    with open(f'{argv[1]}.json', 'w', newline='') as file:
        json.dump(u_tasks, file)
