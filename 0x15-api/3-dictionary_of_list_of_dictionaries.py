#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress and exports data in JSON format.
"""
import json
import requests

if __name__ == '__main__':
    json_filename = "todo_all_employees.json"
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()

    with open(json_filename, "w") as json_file:
        todo_data = {
            user.get("id"): [
                {
                    'username': user.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed')
                }
                for task in todos if user.get("id") == task.get('userId')
            ]
            for user in users
        }
        json.dump(todo_data, json_file)
