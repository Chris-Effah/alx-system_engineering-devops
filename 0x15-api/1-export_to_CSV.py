#!/usr/bin/python3
"""A Python script that gets data from an API and exports it to a CSV format"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Function to get employee to-do list progress

    Args:
        employee_id (int): The employee ID

    Returns:
        list: List containing the employee's completed tasks
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Could not fetch employee details.")
        return None

    user_data = user_response.json()
    employee_name = user_data.get('name', f'Employee {employee_id}')

    response = requests.get(url)

    if response.status_code == 200:
        todo_list = response.json()

        # Filter completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]

        if completed_tasks:
            print(f"Employee {employee_name} completed tasks:")
            for task in completed_tasks:
                print(f"\t{task['title']}")
            return completed_tasks
        else:
            print(f"No completed tasks found for Employee {employee_name}")
            return []
    else:
        print("Error: Could not fetch employee's to-do list.")
        return None

def export_to_csv(tasks, employee_id):
    """
    Function to export employee's completed tasks to a CSV file

    Args:
        tasks (list): List containing completed tasks
        employee_id (int): The employee ID

    Returns:
        None
    """

    if not tasks:
        return

    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": task.get('username', ''),
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        completed_tasks = get_employee_todo_progress(employee_id)
        export_to_csv(completed_tasks, employee_id)

