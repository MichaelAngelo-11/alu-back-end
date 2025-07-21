#!/usr/bin/python3
"""Exports all employees' TODO list data in JSON format"""

import json
import requests

if __name__ == "__main__":
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    # Prepare the final data dictionary
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get this user's tasks
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos = requests.get(todos_url).json()

        # Format each task
        task_list = []
        for task in todos:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_dict)

        all_data[user_id] = task_list

    # Write to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
