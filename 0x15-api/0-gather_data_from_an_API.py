#!/usr/bin/python3
""" makes a request get some stuff """
import requests
from sys import argv


def main(emp_id):
    """ main function"""
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    try:
        user_response = requests.get(users_url.format(emp_id))
        user_response.raise_for_status()
        user = user_response.json()
    except requests.exceptions.HTTPError as e:
        print("Error getting user with ID {}: {}".format(emp_id, e))
        exit(1)
    except ValueError as e:
        print(
            "Error parsing JSON response for user with ID {}: {}"
            .format(emp_id, e))
        exit(1)

    try:
        todos_response = requests.get(todos_url.format(emp_id))
        todos_response.raise_for_status()
        todos = todos_response.json()
    except requests.exceptions.HTTPError as e:
        print("Error getting TODOs for user with ID {}: {}".format(emp_id, e))
        exit(1)
    except ValueError as e:
        print(
            "Error parsing JSON response for TODOs for user with ID {}: {}"
            .format(emp_id, e))
        exit(1)

    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t['completed']]
    num_completed_tasks = len(completed_tasks)
    employee_name = user.get('name', '')

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title', '')))


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)
    main(argv[1])
