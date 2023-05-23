#!/usr/bin/python3
"""
REST API call and processing
"""
import json
import requests
import sys

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    id_ = sys.argv[1]
    user_id = id_
    response = response.json()
    task_list = []
    user = requests.get("https://jsonplaceholder.typicode.com/users/"+str(id_))
    username = user.json()['username']
    for todo in response:
        new_task = {}
        if int(todo['userId']) == int(user_id):
            new_task["task"] = todo['title']
            new_task["completed"] = todo["completed"]
            new_task["username"] = username
            task_list.append(new_task)
    out = {}
    out[str(user_id)] = task_list
    fout = open("{}.json".format(user_id), "w")
    json.dump(out, fout)
