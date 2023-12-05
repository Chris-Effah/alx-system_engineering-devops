#!/usr/bin/python3
"""A bash script accept an integer as a
parameter, which is the employee ID"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0].get('username', '')

        done_tasks = [task for task in todos if task.get('completed', False)]
        num_done_tasks = len(done_tasks)
        total_tasks = len(todos)
        status = "OK" if num_done_tasks > 0 else "Incorrect"

        progress_message = (
            f'Employee Name: {status} '
            f'({num_done_tasks}/{total_tasks}):'
        )
        print(progress_message)

        if done_tasks:
            for task in done_tasks:
                print(f'\t{task.get("title", "")}')
        else:
            print('\tNo completed tasks')

        # Export data to JSON
        export_to_json(employee_id, employee_name, done_tasks)
    else:
        print(f'Error: Unable to fetch TODO list for employee {employee_id}')


def export_to_json(employee_id, employee_name, done_tasks):
    data = {
        "USER_ID": [
            {
                "task": task.get("title", ""),
                "completed": task.get("completed", False),
                "username": employee_name,
            }
            for task in done_tasks
        ]
    }

    filename = f'{employee_id}.json'

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
