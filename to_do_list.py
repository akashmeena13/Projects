def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def remove_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Invalid task number!")

tasks = []
while True:
    print("\nOptions:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        show_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
