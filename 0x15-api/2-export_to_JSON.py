#!/usr/bin/python3
""" makes a request get some stuff """
import json
import requests
from sys import argv, exit


def main(emp_id):
    """ main function"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error: User not found')
        exit(1)

    user_data = response.json()
    username = user_data.get('username')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(emp_id)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error: Could not fetch tasks')
        exit(1)

    tasks = response.json()
    tasks_data = {'{}'.format(emp_id): []}
    for task in tasks:
        tasks_data[emp_id].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    # Write to JSON file
    filename = '{}.json'.format(emp_id)
    with open(filename, 'w') as f:
        json.dump(tasks_data, f)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)
    main(argv[1])
