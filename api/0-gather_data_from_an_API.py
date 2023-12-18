#!/usr/bin/python3
"""Gather data from API"""

from sys import argv
import requests

if __name__ == '__main__':
    c_todo = 0
    c_complete = 0
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    if users.status_code == 200 and todos.status_code == 200:
        for todo in todos.json():
            c_todo += 1
            if todo['completed'] is True:
                c_complete += 1
        name = users.json()['name']
        print(f'Employee {name} is done with tasks({c_complete}/{c_todo}):')
        for task in todos.json():
            if task['completed'] is True:
                title = task['title']
                print(f'\t {title}')
