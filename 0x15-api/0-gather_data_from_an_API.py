#!/usr/bin/python3
"""
REST API call and processing
"""
import requests
import sys
import json
if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    id_ = sys.argv[1]
    user_id = id_
    response = response.json()
    not_completed = []
    completed = []
    for todo in response:
        if int(todo['userId']) == int(user_id):
            if todo['completed']:
                completed.append(todo)
            else:
                not_completed.append(todo)
    total = len(not_completed) + len(completed)
    user = requests.get("https://jsonplaceholder.typicode.com/users/"+str(id_))
    employeeName = user.json()['name']
    A = len(completed)
    B = total
    print("Employee {} is done with tasks({}/{}):".format(employeeName, A, B))
    for task in completed:
        print("\t {}".format(task['title']))
