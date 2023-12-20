#!/usr/bin/python3
"""API to csv format"""

import requests
from sys import argv
import csv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user = requests.get(f'{API_URL}/users/{argv[1]}').json()
    todo_list = requests.get(f"{API_URL}/todos?userId={argv[1]}").json()

    with open( f"{argv[1]}.csv", mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            csv_writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])
