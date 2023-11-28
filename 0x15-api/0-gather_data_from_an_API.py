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

    response = requests.get(url)

    if response.status_code == 200:
        todo_list = response.json()

        employee_name = todo_list[0].get('username', '')

        TOTAL_NUMBER_OF_TASKS = len(todo_list)
        NUMBER_OF_DONE_TASKS = sum(1 for task in todo_list
                                   if task['completed'])
        status = "OK" if TOTAL_NUMBER_OF_TASKS > 0 else "Incorrect"

        print(f"Employee {employee_name} is done with tasks "
              f"({NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS}): ")
        print(f"{employee_name}: "
              f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}")
        print("NUMBER_OF_DONE_TASKS:")

        for task in todo_list:
            if task['completed']:
                print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
