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
    user = requests.get("https://jsonplaceholder.typicode.com/users/"+str(id_))
    username = user.json()['username']
    fileout = open("{}.csv".format(user_id), "w")
    for todo in response:
        if int(todo['userId']) == int(user_id):
            status = todo['completed']
            title = todo['title']
            f = '"{}","{}","{}","{}"\n'.format(user_id, username,
                                               status, title)
            fileout.write(f)
