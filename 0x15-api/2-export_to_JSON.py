#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress and exports data in JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user_info_url = base_url + "users/{}".format(employee_id)
    user_info = requests.get(user_info_url).json()

    todos_url = base_url + "todos?userId={}".format(employee_id)
    todos = requests.get(todos_url).json()

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, "w") as json_file:
        json.dump({employee_id: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user_info.get('username')
        } for task in todos]}, json_file)
