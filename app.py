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
def add_task(tasks):
    name = input("what is the task name? ")
    description = input("What the task's description?")
    due_date = input("what is the due date? this format please(YYYY-MM-DD)")
    priority = input ("what is the priority")

    task ={
        "name": name,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        'status': "pending"
    }


    tasks.append(task)
    save_tasks(tasks)

# view tasks

def view_tasks(tasks):
    if not tasks:
        print(("There are no tasks to dislpay."))
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"\nTask {index}:")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")


# mark as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_id = int(input("What the task nuber that you want to mark as completed"))
    if 0 <= task_id < len(tasks):
        tasks[task_id]['status'] = 'completed'
        save_tasks(tasks)
        print("your task was marked as completed")
    else:
        print("Invalid task number")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("What the task nuber that you want to delete"))
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("your task was deleted")
    else:
        print("Invalid task number")


# the main loop
def main():
    tasks = load_tasks()


    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("cChoose one of the options")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid option ")

if __name__ == "__main__":
    main()

