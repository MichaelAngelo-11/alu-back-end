#!/usr/bin/python3
"""Export an employee's TODO list to JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()
    username = user_response.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos_response
    ]

    data = {employee_id: tasks}
    filename = f"{employee_id}.json"

    with open(filename, "w") as json_file:
        json.dump(data, json_file)
