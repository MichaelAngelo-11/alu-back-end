#!/usr/bin/python3
""" Script that fetches and displays the TODO list progress for a given employee ID """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_info = requests.get(url).json()
    if not user_info:
        print("User not found.")
        sys.exit(1)

    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")
    completed_tasks = [task for task in todo_info if task.get("completed") is True]
    total_tasks = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks
    ))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

