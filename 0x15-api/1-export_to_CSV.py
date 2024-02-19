#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress and exports data in CSV format.
"""
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    user_response = requests.get(user_url).json()
    username = user_response.get("username")

    todos_url = ('https://jsonplaceholder.typicode.com/users/' +
                 employee_id + '/todos')
    todos_response = requests.get(todos_url)

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos_response.json():
            task_completed = todo.get("completed")
            task_title = todo.get("title")
            csv_writer.writerow([employee_id, username,
                                 task_completed, task_title])
