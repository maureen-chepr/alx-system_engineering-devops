#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    # Get employee ID from command line argument
    employee_id = sys.argv[1]

    # Lists to store task titles and count completed tasks
    completed_task_titles = []
    completed_tasks_count = 0
    total_tasks_count = 0

    # URL for fetching employee information
    user_url = "https://jsonplaceholder.typicode.com/users/" + employee_id
    user_response = requests.get(user_url).json()
    employee_name = user_response.get('name')

    # URL for fetching tasks
    tasks_url = "https://jsonplaceholder.typicode.com/todos/"
    tasks_response = requests.get(tasks_url).json()

    # Iterate through tasks to calculate progress
    for task in tasks_response:
        if task.get('userId') == int(employee_id):
            if task.get('completed'):
                completed_task_titles.append(task['title'])
                completed_tasks_count += 1
            total_tasks_count += 1

    # Display progress information
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks_count, total_tasks_count))

    # Display titles of completed tasks
    for title in completed_task_titles:
        print("\t {}".format(title))
