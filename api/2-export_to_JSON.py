#!/usr/bin/python3
"""
fgbvd
"""
import json
import requests
from sys import argv


def get_info(url):
    data = requests.get(url)
    return data.json()


def export_to_json(employee_id, todos):
    """
    Export TODO list to a JSON file
    """
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump({employee_id: todos}, file)


def main(employee_id):
    """
    fgbjfnd
    """
    api_url = "https://jsonplaceholder.typicode.com/users"
    employee_info_url = f"{api_url}/{employee_id}/"

    employee_todo_url = f"{api_url}/{employee_id}/todos"

    employee_info = get_info(employee_info_url)
    employee_todo = get_info(employee_todo_url)

    username = employee_info.get("username")

    export_to_json(employee_id, employee_todo)


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
