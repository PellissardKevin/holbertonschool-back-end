#!/usr/bin/python3
"""API to csv format"""

import requests
from sys import argv
import csv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    USER_ID = argv[1]
    user = requests.get(f'{API_URL}/users/{USER_ID}').json()
    todo_list = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    with open(f"{USER_ID}.csv", mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            csv_writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])

    print(f"Data has been exported to {USER_ID}.csv")
