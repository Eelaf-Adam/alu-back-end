#!/usr/bin/python3
"""
Exports all employees' TODO list data to a JSON file.

The JSON file is a dictionary mapping USER_IDs (as strings),
to lists of task dictionaries:
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  ...
}

Output file: todo_all_employees.json
"""

import json
import requests
import sys


def fetch_all_users():
    """Fetch all users from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    return response.json()


def fetch_all_todos():
    """Fetch all todos from the API."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit(1)
    return response.json()


def build_todo_dict(users, todos):
    """Build dictionary mapping user IDs to list of their task dicts."""
    user_dict = {str(user.get("id")): user.get("username") for user in users}
    result = {}

    for todo in todos:
        user_id = str(todo.get("userId"))
        username = user_dict.get(user_id)
        if username is None:
            continue  # skip if user not found

        task_dict = {
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        }

        if user_id not in result:
            result[user_id] = []
        result[user_id].append(task_dict)

    return result


def export_to_json(data, filename="todo_all_employees.json"):
    """Write the data dictionary to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    users = fetch_all_users()
    todos = fetch_all_todos()
    todo_dict = build_todo_dict(users, todos)
    export_to_json(todo_dict)
