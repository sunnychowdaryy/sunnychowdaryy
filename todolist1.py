import os

tasks = []

def display_tasks():
    if not tasks:
        print("To-do list is Empty.\n")
    else:
        print("To-do list.")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"The task added is: {task}")

def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index -1] = new_task
        print(f"Task no. {index} updated to {new_task}")
    else:
        print("The task number is invalid")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"The task no. {index} is removed successfully")
    else:
        print("The task number is invalid")

def delete_task():
    global tasks
    tasks = []

while True:
    os.system("clear" if os.name == "posix" else "cls")
    print("///// To-Do List Application /////\n")
    display_tasks()
    print("Select any one option.")
    print("1. Add New Task.")
    print("2. Update New Task.")
    print("3. Remove Existing Task.")
    print("4. Delete all Tasks.")
    print("5. Exit.\n")

    select = input("What do you wanna do? ")
    if select == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif select == "2":
        index = int(input("Which task do you want to update? Enter the number."))
        new_task = input("Enter the new updated task: ")
        update_task(index, new_task)
    elif select == "3":
        index = int(input("Which task do you want to remove? Enter the number."))
        remove_task(index)
    elif select == "4":
        delete_task()
        print("All tasks have been deleted.")
    elif select == "5":
        print("Exiting the Application")
        break
    else:
        input("Invalid choice. Enter any button to continue.....")

with open("Save.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")