#!/usr/bin/python3
"""
Script that returns TODO list progress for a given employee ID
using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    emp_id = sys.argv[1]

    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee information
    user = requests.get(f"{base_url}/users/{emp_id}").json()

    # Fetch employee TODOs
    todos = requests.get(f"{base_url}/todos", params={"userId": emp_id}).json()

    # Extract needed data
    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    # Print output
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

