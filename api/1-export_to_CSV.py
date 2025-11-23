#!/usr/bin/python3
"""
Exports data for a given employee ID to CSV format.
"""

import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user and tasks
    user_res = requests.get(user_url)
    todos_res = requests.get(todos_url)

    if user_res.status_code != 200 or todos_res.status_code != 200:
        sys.exit(1)

    user = user_res.json()
    todos = todos_res.json()

    username = user.get("username")
    if not username:
        sys.exit(1)

    filename = f"{employee_id}.csv"

    # Write CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(
            f, 
            quoting=csv.QUOTE_ALL  # ensures double quotes
        )

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

