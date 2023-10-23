#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    This function takes the employee ID as a parameter and will
    retrieve and display the employee's TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data['name']

        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        p_m = f"Employee {employee_name} is done with tasks
        ({completed_tasks}/{total_tasks}): "
        print(p_m)
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)


if __name__ == "__main__":
    """
    calling the main function
    """
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))
