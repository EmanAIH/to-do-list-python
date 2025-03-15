# To do list

import json
from datetime import datetime

# add task:

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks =[]
    return tasks

# Save tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
      json.dump(tasks, file, indent=4)  

# add new task
