#!/usr/bin/python3
"""API to csv format"""

import requests
from sys import argv
import csv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    todos = requests.get(f'{API_URL}/users/{argv[1]}/todos',
                         arams={"_expand": "user"})
    username = todos.json()[0]['user']['username']
    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos.json():
            writer.writerow(
                [argv[1], username, str(todo['completed']), todo['title']])
