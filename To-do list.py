#TO-DO LIST
#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

tasks = []

def show_tasks():
  if tasks:
    for index, task in enumerate(tasks):
      print(f"{index + 1}. {task}")
  else:
    print("Your to-do list is empty.")


def add_task():
  task_name = input("Enter a task to add: ")
  tasks.append(task_name)
  print("Task added successfully!")


def remove_task():
  show_tasks()
  if tasks:
    try:
      task_index = int(input("Enter the number of the task to remove: ")) - 1
      tasks.pop(task_index)
      print("Task removed successfully!")
    except IndexError:
      print("Invalid task number.")


while True:
  print("\nTo-Do List Menu:")
  print("1. Show Tasks")
  print("2. Add Task")
  print("3. Remove Task")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    show_tasks()
  elif choice == '2':
    add_task()
  elif choice == '3':
    remove_task()
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please try again.")

print("Exiting To-Do List...")
