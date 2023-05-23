#!/usr/bin/python3
"""
REST API call and processing
"""
import json
import requests
import sys

if __name__ == "__main__":
    users_dict = {}
    users = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users.json()
    for user in users:
        users_dict[user['id']] = user['username']
    all_dict = {}

    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos.json()

    for todo in todos:
        new_task = {}
        user_id = todo['userId']
        new_task["username"] = users_dict.get(user_id, "")
        new_task["task"] = todo['title']
        new_task["completed"] = todo["completed"]
        if not all_dict.get(user_id, None):
            all_dict[user_id] = [new_task]
        else:
            all_dict[user_id].append(new_task)
    fout = open("todo_all_employees.json", "w")
    json.dump(all_dict, fout)
