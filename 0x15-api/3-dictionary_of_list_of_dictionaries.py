#!/usr/bin/python3
""" makes a request get some stuff """
import json
import requests
from sys import exit


def main():
    """ main function"""
    url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Get todos and users data
    todos_response = requests.get(url)
    users_response = requests.get(users_url)

    # Check response status code
    if todos_response.status_code != 200 or users_response.status_code != 200:
        print("Error: Could not retrieve data from API")
        exit()

    todos_data = todos_response.json()
    users_data = users_response.json()

    # Create dictionary with users data
    users_dict = {}
    for user in users_data:
        user_id = user.get('id', '')
        user_name = user.get('username', '')
        users_dict[user_id] = {"name": user_name, "tasks": []}

    # Add tasks to users dictionary
    for task in todos_data:
        task_dict = {"username": users_dict[task["userId"]]["name"],
                     "task": task["title"],
                     "completed": task["completed"]}
        users_dict[task["userId"]]["tasks"].append(task_dict)

    # Write JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(users_dict, json_file)


if __name__ == '__main__':
    main()
