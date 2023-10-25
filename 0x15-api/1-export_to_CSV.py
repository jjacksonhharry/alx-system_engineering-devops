#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to CSV.
"""

import requests
import sys


if __name__ == "__main":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    response = requests.get(url)
    employeeData = response.json()
    employeeName = employeeData.get('name')
    username = employeeData.get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    # Create a CSV file for the user
    csv_file = f"{employeeId}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])

        for task in tasks:
            task_title = task.get('title')
            task_completed = task.get('completed')
            writer.writerow([
                employeeId,
                username,
                task_completed,
                task_title])

    print
    (f"Employee {employeeName} is done with tasks ({len(tasks)} in total).")
    print(f"Data has been exported to {csv_file}.")
