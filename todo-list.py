# Define an empty list to store tasks
tasks = []

# Adds a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

# User can view his tasks
def view_tasks():
    if not tasks:
        print("Your todo list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Mark task as completed
def complete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            completed_task = tasks.pop(task_index)
            print(f"Task '{completed_task}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Program logic
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option(1-4)")
