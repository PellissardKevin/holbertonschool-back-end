#!/usr/bin/python3
"""API to csv format"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos",
        params={"_expand": "user"},
    )
    username = todos.json()[0]["user"]["username"]
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos.json():
            csv_writer.writerow(
                [user["id"],
                user["username"],
                task["completed"],
                task["title"]]
            )
