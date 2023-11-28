#!/usr/bin/python3
"""a python script that gets data drom an api"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    function to get employee to do list progress

    Args:
        employee_id(int): the employee ID

    Returns:
        None
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Could not fetch employee details.")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name', f'Employee {employee_id}')

    response = requests.get(url)

    if response.status_code == 200:
        todo_list = response.json()

        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])

        if total_tasks > 0:
            progress_ratio = f"({completed_tasks}/{total_tasks})"
        else:
            progress_ratio = "(No tasks)"

        print(f"Employee {employee_name} is done with tasks{progress_ratio}: ")
        print(f"Number of completed tasks: {completed_tasks}/{total_tasks}")

        for task in todo_list:
            if task['completed']:
                print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
