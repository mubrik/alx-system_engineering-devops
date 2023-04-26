#!/usr/bin/python3
""" makes a request get some stuff """
import csv
import requests
from sys import argv


def main(emp_id):
    """ main function"""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id))
    user = response.json()
    username = user.get('username', '')

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id))
    todos = response.json()

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [emp_id, username,
                 str(todo.get('completed', '')), todo.get('title', '')])


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)
    main(argv[1])
